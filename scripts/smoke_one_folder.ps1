$ErrorActionPreference = "Stop"

$repo = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$dist = Join-Path $repo "dist"
$tempParent = Join-Path $repo "tests/.tmp"
$tempRoot = Join-Path $tempParent ("one-folder-" + [guid]::NewGuid().ToString("N"))

$packages = @(
    @{ Archive = "AI-Agent-Tool-Codex.zip"; Root = ".agents"; Sentinel = "skills/existing/SKILL.md"; Required = "skills/ai-agent-tool/SKILL.md" },
    @{ Archive = "AI-Agent-Tool-Claude-Code.zip"; Root = ".claude"; Sentinel = "rules/existing.md"; Required = "skills/agent-birth/SKILL.md" },
    @{ Archive = "AI-Agent-Tool-Claude-Cowork.zip"; Root = "AI-Agent-Tool"; Sentinel = "existing-user-file.md"; Required = "skill/agent-birth/SKILL.md" },
    @{ Archive = "AI-Agent-Tool-Gemini-CLI.zip"; Root = ".gemini"; Sentinel = "settings.json"; Required = "agents/ai-agent-tool.md" },
    @{ Archive = "AI-Agent-Tool-GitHub-Copilot.zip"; Root = ".github"; Sentinel = "copilot-instructions.md"; Required = "skills/agent-birth/SKILL.md" },
    @{ Archive = "AI-Agent-Tool-OpenClaw.zip"; Root = "skills"; Sentinel = "existing/SKILL.md"; Required = "agents/SKILL.md" }
)

function Assert-True {
    param(
        [bool]$Condition,
        [string]$Message
    )
    if (-not $Condition) {
        throw $Message
    }
}

New-Item -ItemType Directory -Force -Path $tempRoot | Out-Null

try {
    Add-Type -AssemblyName System.IO.Compression.FileSystem

    foreach ($package in $packages) {
        $archivePath = Join-Path $dist $package.Archive
        Assert-True (Test-Path -LiteralPath $archivePath -PathType Leaf) "Missing archive: $($package.Archive)"

        $archive = [System.IO.Compression.ZipFile]::OpenRead($archivePath)
        try {
            $roots = @(
                $archive.Entries |
                    Where-Object { -not [string]::IsNullOrWhiteSpace($_.Name) } |
                    ForEach-Object { $_.FullName.Replace("\", "/").Split("/")[0] } |
                    Sort-Object -Unique
            )
        }
        finally {
            $archive.Dispose()
        }

        Assert-True ($roots.Count -eq 1) "$($package.Archive) exposes $($roots.Count) top-level items"
        Assert-True ($roots[0] -eq $package.Root) "$($package.Archive) exposes '$($roots[0])' instead of '$($package.Root)'"

        $project = Join-Path $tempRoot ([IO.Path]::GetFileNameWithoutExtension($package.Archive))
        $installRoot = Join-Path $project $package.Root
        $sentinel = Join-Path $installRoot $package.Sentinel
        New-Item -ItemType Directory -Force -Path (Split-Path -Parent $sentinel) | Out-Null
        [IO.File]::WriteAllText($sentinel, "preserve-existing", [Text.UTF8Encoding]::new($false))

        Expand-Archive -LiteralPath $archivePath -DestinationPath $project -Force

        Assert-True (Test-Path -LiteralPath $sentinel -PathType Leaf) "Existing file disappeared while merging $($package.Archive)"
        Assert-True ((Get-Content -LiteralPath $sentinel -Raw) -eq "preserve-existing") "Existing file changed while merging $($package.Archive)"
        Assert-True (Test-Path -LiteralPath (Join-Path $installRoot $package.Required) -PathType Leaf) "Required adapter file missing after merge: $($package.Archive)"
    }

    Write-Output "PASS: $($packages.Count) one-folder archives merge without removing unrelated existing files"
}
finally {
    $resolvedTemp = [IO.Path]::GetFullPath($tempRoot)
    $resolvedParent = [IO.Path]::GetFullPath($tempParent)
    if (-not $resolvedTemp.StartsWith($resolvedParent + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing to clean temporary path outside tests/.tmp: $resolvedTemp"
    }
    if (Test-Path -LiteralPath $resolvedTemp) {
        Remove-Item -LiteralPath $resolvedTemp -Recurse -Force
    }
}
