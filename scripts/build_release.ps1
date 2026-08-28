param(
    [string]$Version = ""
)

$ErrorActionPreference = "Stop"
$repo = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$dist = Join-Path $repo "dist"
$declaredVersion = (Get-Content -LiteralPath (Join-Path $repo "VERSION") -Raw).Trim()
$platforms = [ordered]@{
    "codex"          = "AI-Agent-Tool-Codex.zip"
    "claude-code"    = "AI-Agent-Tool-Claude-Code.zip"
    "claude-cowork"  = "AI-Agent-Tool-Claude-Cowork.zip"
    "gemini-cli"     = "AI-Agent-Tool-Gemini-CLI.zip"
    "github-copilot" = "AI-Agent-Tool-GitHub-Copilot.zip"
    "openclaw"       = "AI-Agent-Tool-OpenClaw.zip"
}

if ([string]::IsNullOrWhiteSpace($Version)) {
    $Version = $declaredVersion
}
if ($Version -ne $declaredVersion) {
    throw "Requested version $Version does not match VERSION $declaredVersion."
}
if ($Version -notmatch '^\d+\.\d+\.\d+$') {
    throw "Invalid release version: $Version"
}

python (Join-Path $PSScriptRoot "validate_bundles.py")
if ($LASTEXITCODE -ne 0) {
    throw "Bundle validation failed."
}

New-Item -ItemType Directory -Force -Path $dist | Out-Null
$resolvedDist = [System.IO.Path]::GetFullPath($dist)

Get-ChildItem -LiteralPath $dist -File | Where-Object {
    $_.Name -match '^(?i:ai-agent-tool-).+\.zip$' -or $_.Name -eq 'SHA256SUMS.txt'
} | ForEach-Object {
    $candidate = [System.IO.Path]::GetFullPath($_.FullName)
    if (-not $candidate.StartsWith($resolvedDist + [System.IO.Path]::DirectorySeparatorChar, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing to remove artifact outside dist: $candidate"
    }
    Remove-Item -LiteralPath $candidate -Force
}

Add-Type -AssemblyName System.IO.Compression.FileSystem
Add-Type -AssemblyName System.IO.Compression

function New-TemporaryRoot {
    $path = Join-Path ([System.IO.Path]::GetTempPath()) ("ai-agent-tool-" + [guid]::NewGuid().ToString("N"))
    New-Item -ItemType Directory -Path $path | Out-Null
    return $path
}

function Remove-TemporaryRoot {
    param([string]$Path)

    $resolvedTemp = [System.IO.Path]::GetFullPath($Path)
    $systemTemp = [System.IO.Path]::GetFullPath([System.IO.Path]::GetTempPath())
    if (-not $resolvedTemp.StartsWith($systemTemp, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing to remove temporary directory outside system temp: $resolvedTemp"
    }
    if (Test-Path -LiteralPath $resolvedTemp) {
        Remove-Item -LiteralPath $resolvedTemp -Recurse -Force
    }
}

function Add-GitFilesToDirectory {
    param(
        [string]$Prefix,
        [string]$DestinationRoot,
        [switch]$StripPrefix,
        [string]$ArchivePrefix = ""
    )

    $files = @(git -C $repo ls-files --cached --others --exclude-standard -- $Prefix)
    if ($LASTEXITCODE -ne 0) {
        throw "Unable to enumerate Git files for $Prefix"
    }
    if ($files.Count -eq 0) {
        throw "No release files found for $Prefix"
    }

    $prefixBase = $Prefix.TrimEnd("/")
    foreach ($relative in $files) {
        if ([string]::IsNullOrWhiteSpace($relative)) { continue }
        $normalized = $relative.Replace("/", [System.IO.Path]::DirectorySeparatorChar)
        $source = Join-Path $repo $normalized
        if (-not (Test-Path -LiteralPath $source -PathType Leaf)) { continue }

        if ($StripPrefix) {
            $archiveRelative = $relative.Substring($prefixBase.Length).TrimStart("/")
        }
        else {
            $archiveRelative = $relative
        }
        if (-not [string]::IsNullOrWhiteSpace($ArchivePrefix)) {
            $archiveRelative = "$ArchivePrefix/$archiveRelative"
        }

        $target = Join-Path $DestinationRoot $archiveRelative.Replace("/", [System.IO.Path]::DirectorySeparatorChar)
        New-Item -ItemType Directory -Force -Path (Split-Path -Parent $target) | Out-Null
        Copy-Item -LiteralPath $source -Destination $target -Force
    }
}

function Compress-Directory {
    param(
        [string]$SourceRoot,
        [string]$Output
    )

    $resolvedOutput = [System.IO.Path]::GetFullPath($Output)
    if (-not $resolvedOutput.StartsWith($resolvedDist + [System.IO.Path]::DirectorySeparatorChar, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing to write release artifact outside dist: $resolvedOutput"
    }
    if ([System.IO.File]::Exists($resolvedOutput)) {
        [System.IO.File]::Delete($resolvedOutput)
    }

    $stream = [System.IO.File]::Open($resolvedOutput, [System.IO.FileMode]::CreateNew)
    $archive = [System.IO.Compression.ZipArchive]::new($stream, [System.IO.Compression.ZipArchiveMode]::Create, $false)
    try {
        foreach ($file in Get-ChildItem -LiteralPath $SourceRoot -File -Recurse -Force | Sort-Object FullName) {
            $entryName = $file.FullName.Substring($SourceRoot.Length).TrimStart("\", "/").Replace("\", "/")
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

function New-ZipFromGitFiles {
    param(
        [string]$Prefix,
        [string]$Output,
        [switch]$StripPrefix,
        [string]$ArchivePrefix = ""
    )

    $tempRoot = New-TemporaryRoot
    try {
        Add-GitFilesToDirectory `
            -Prefix $Prefix `
            -DestinationRoot $tempRoot `
            -StripPrefix:$StripPrefix `
            -ArchivePrefix $ArchivePrefix
        Compress-Directory -SourceRoot $tempRoot -Output $Output
    }
    finally {
        Remove-TemporaryRoot -Path $tempRoot
    }
}

foreach ($platform in $platforms.Keys) {
    $output = Join-Path $dist $platforms[$platform]
    New-ZipFromGitFiles -Prefix "$platform/" -Output $output -StripPrefix
}

$hashLines = Get-ChildItem -LiteralPath $dist -Filter "*.zip" | Sort-Object Name | ForEach-Object {
    $hash = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
    "$hash  $($_.Name)"
}
[System.IO.File]::WriteAllLines((Join-Path $dist "SHA256SUMS.txt"), $hashLines, [System.Text.UTF8Encoding]::new($false))

Get-ChildItem -LiteralPath $dist | Sort-Object Name | Select-Object Name, Length
