param(
    [string]$Version = "2.0.0"
)

$ErrorActionPreference = "Stop"
$repo = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$dist = Join-Path $repo "dist"
$bundles = @("codex", "claude-code", "claude-cowork", "gemini-cli", "github-copilot", "openclaw")

python (Join-Path $PSScriptRoot "validate_bundles.py")
if ($LASTEXITCODE -ne 0) {
    throw "Bundle validation failed."
}

New-Item -ItemType Directory -Force -Path $dist | Out-Null
Add-Type -AssemblyName System.IO.Compression.FileSystem
Add-Type -AssemblyName System.IO.Compression

function New-ZipFromGitFiles {
    param(
        [string]$Prefix,
        [string]$Output,
        [switch]$StripPrefix
    )

    $tempRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("ai-agent-tool-" + [guid]::NewGuid().ToString("N"))
    New-Item -ItemType Directory -Path $tempRoot | Out-Null
    try {
        $files = git -C $repo ls-files --cached --others --exclude-standard -- $Prefix
        foreach ($relative in $files) {
            if ([string]::IsNullOrWhiteSpace($relative)) { continue }
            $normalized = $relative.Replace("/", [System.IO.Path]::DirectorySeparatorChar)
            $source = Join-Path $repo $normalized
            if (-not (Test-Path -LiteralPath $source -PathType Leaf)) { continue }
            if ($StripPrefix) {
                $zipRelative = $relative.Substring($Prefix.TrimEnd("/").Length).TrimStart("/")
            } else {
                $zipRelative = $relative
            }
            $target = Join-Path $tempRoot $zipRelative.Replace("/", [System.IO.Path]::DirectorySeparatorChar)
            New-Item -ItemType Directory -Force -Path (Split-Path -Parent $target) | Out-Null
            Copy-Item -LiteralPath $source -Destination $target -Force
        }

        if ([System.IO.File]::Exists($Output)) {
            [System.IO.File]::Delete($Output)
        }
        $stream = [System.IO.File]::Open($Output, [System.IO.FileMode]::CreateNew)
        $archive = [System.IO.Compression.ZipArchive]::new($stream, [System.IO.Compression.ZipArchiveMode]::Create, $false)
        try {
            foreach ($file in Get-ChildItem -LiteralPath $tempRoot -File -Recurse | Sort-Object FullName) {
                $entryName = $file.FullName.Substring($tempRoot.Length).TrimStart("\", "/").Replace("\", "/")
                [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile(
                    $archive,
                    $file.FullName,
                    $entryName,
                    [System.IO.Compression.CompressionLevel]::Optimal
                ) | Out-Null
            }
        }
        finally {
            $archive.Dispose()
            $stream.Dispose()
        }
    }
    finally {
        $resolvedTemp = [System.IO.Path]::GetFullPath($tempRoot)
        $systemTemp = [System.IO.Path]::GetFullPath([System.IO.Path]::GetTempPath())
        if ($resolvedTemp.StartsWith($systemTemp, [System.StringComparison]::OrdinalIgnoreCase) -and (Test-Path -LiteralPath $resolvedTemp)) {
            Remove-Item -LiteralPath $resolvedTemp -Recurse -Force
        }
    }
}

foreach ($bundle in $bundles) {
    $prefix = "bundles/$bundle/"
    $output = Join-Path $dist "ai-agent-tool-$bundle-v$Version.zip"
    New-ZipFromGitFiles -Prefix $prefix -Output $output -StripPrefix
}

$coworkSkillPrefix = "bundles/claude-cowork/cowork-skill/agent-birth/"
$coworkSkillOutput = Join-Path $dist "ai-agent-tool-claude-cowork-skill-v$Version.zip"
New-ZipFromGitFiles -Prefix $coworkSkillPrefix -Output $coworkSkillOutput -StripPrefix

$sourceOutput = Join-Path $dist "ai-agent-tool-v$Version.zip"
New-ZipFromGitFiles -Prefix "." -Output $sourceOutput

$hashLines = Get-ChildItem -LiteralPath $dist -Filter "*.zip" | Sort-Object Name | ForEach-Object {
    $hash = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
    "$hash  $($_.Name)"
}
[System.IO.File]::WriteAllLines((Join-Path $dist "SHA256SUMS.txt"), $hashLines, [System.Text.UTF8Encoding]::new($false))

Get-ChildItem -LiteralPath $dist | Sort-Object Name | Select-Object Name, Length
