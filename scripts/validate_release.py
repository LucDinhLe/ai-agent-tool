#!/usr/bin/env python3
"""Validate built AI Agent Tool release archives without extracting them."""

from __future__ import annotations

import hashlib
import re
import sys
import zipfile
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

PLATFORMS = {
    "codex": (
        "01-CODEX",
        {"AGENTS.md", ".agents/skills/agents/SKILL.md", ".ai-agent/VERSION"},
    ),
    "claude-code": (
        "02-CLAUDE-CODE",
        {"CLAUDE.md", ".claude/skills/agent-birth/SKILL.md", ".ai-agent/VERSION"},
    ),
    "claude-cowork": (
        "03-CLAUDE-COWORK",
        {
            "COWORK-PROJECT-INSTRUCTIONS.txt",
            "cowork-skill/agent-birth/SKILL.md",
            ".ai-agent/VERSION",
        },
    ),
    "gemini-cli": (
        "04-GEMINI-CLI",
        {"GEMINI.md", ".gemini/agents/agents.md", ".agents/skills/agent-birth/SKILL.md"},
    ),
    "github-copilot": (
        "05-GITHUB-COPILOT",
        {
            ".github/copilot-instructions.md",
            ".github/skills/agent-birth/SKILL.md",
            ".ai-agent/VERSION",
        },
    ),
    "openclaw": (
        "06-OPENCLAW",
        {"BOOTSTRAP.md", ".agents/skills/agents/SKILL.md", ".ai-agent-tool/VERSION"},
    ),
}

ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expected_zip_names() -> set[str]:
    names = {f"ai-agent-tool-{name}-v{VERSION}.zip" for name in PLATFORMS}
    names |= {
        f"ai-agent-tool-claude-cowork-skill-v{VERSION}.zip",
        f"AI-Agent-Tool-CHON-NEN-TANG-v{VERSION}.zip",
        f"ai-agent-tool-source-v{VERSION}.zip",
    }
    return names


def validate_safe_entries(archive_name: str, names: list[str]) -> None:
    if len(names) != len(set(names)):
        fail(f"duplicate ZIP entry: {archive_name}")

    for name in names:
        path = PurePosixPath(name)
        normalized = f"/{name.lower()}"
        if "\\" in name or name.startswith("/") or re.match(r"^[a-zA-Z]:", name):
            fail(f"unsafe absolute or Windows path in {archive_name}: {name}")
        if ".." in path.parts:
            fail(f"path traversal in {archive_name}: {name}")
        if "/.ai-agent/private/" in normalized or "/private.example/" in normalized:
            fail(f"private memory included in {archive_name}: {name}")
        if "/tests/.tmp/" in normalized or path.name.lower() == ".env":
            fail(f"private or temporary file included in {archive_name}: {name}")


def read_archive(path: Path) -> set[str]:
    try:
        with zipfile.ZipFile(path) as archive:
            names = [info.filename for info in archive.infolist() if not info.is_dir()]
            validate_safe_entries(path.name, names)
            corrupt = archive.testzip()
            if corrupt:
                fail(f"CRC failure in {path.name}: {corrupt}")
            return set(names)
    except (OSError, zipfile.BadZipFile) as exc:
        fail(f"cannot read {path.name}: {exc}")
        return set()


def require_entries(archive_name: str, names: set[str], required: set[str]) -> None:
    for entry in sorted(required):
        if entry not in names:
            fail(f"missing from {archive_name}: {entry}")


def validate_archives() -> None:
    expected = expected_zip_names()
    actual = {path.name for path in DIST.glob("*.zip")}
    if actual != expected:
        for name in sorted(expected - actual):
            fail(f"missing release ZIP: {name}")
        for name in sorted(actual - expected):
            fail(f"unexpected or stale release ZIP: {name}")

    archives = {name: read_archive(DIST / name) for name in sorted(expected) if (DIST / name).is_file()}

    for platform, (_, required) in PLATFORMS.items():
        archive_name = f"ai-agent-tool-{platform}-v{VERSION}.zip"
        require_entries(
            archive_name,
            archives.get(archive_name, set()),
            {"AI-AGENT-TOOL.md"} | required,
        )

    skill_name = f"ai-agent-tool-claude-cowork-skill-v{VERSION}.zip"
    require_entries(skill_name, archives.get(skill_name, set()), {"SKILL.md", "agents/openai.yaml"})

    all_name = f"AI-Agent-Tool-CHON-NEN-TANG-v{VERSION}.zip"
    all_entries = archives.get(all_name, set())
    expected_roots = {"00-BAT-DAU-O-DAY.md", "VERSION", "LICENSE"}
    expected_roots |= {label for label, _ in PLATFORMS.values()}
    actual_roots = {PurePosixPath(name).parts[0] for name in all_entries}
    if actual_roots != expected_roots:
        fail(f"wrong top-level layout in {all_name}: {sorted(actual_roots)}")
    if any(name.startswith("bundles/") for name in all_entries):
        fail(f"obsolete bundles/ wrapper found in {all_name}")
    for _, (label, required) in PLATFORMS.items():
        require_entries(
            all_name,
            all_entries,
            {f"{label}/AI-AGENT-TOOL.md"} | {f"{label}/{entry}" for entry in required},
        )

    source_name = f"ai-agent-tool-source-v{VERSION}.zip"
    source_entries = archives.get(source_name, set())
    if any(name.startswith("bundles/") for name in source_entries):
        fail(f"obsolete bundles/ wrapper found in {source_name}")
    for platform, (_, required) in PLATFORMS.items():
        require_entries(
            source_name,
            source_entries,
            {f"{platform}/AI-AGENT-TOOL.md"}
            | {f"{platform}/{entry}" for entry in required},
        )


def validate_checksums() -> None:
    checksum_path = DIST / "SHA256SUMS.txt"
    if not checksum_path.is_file():
        fail("missing SHA256SUMS.txt")
        return

    rows: dict[str, str] = {}
    for line in checksum_path.read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+\.zip)", line)
        if not match:
            fail(f"invalid checksum row: {line!r}")
            continue
        digest, name = match.groups()
        if name in rows:
            fail(f"duplicate checksum row: {name}")
        rows[name] = digest

    expected = expected_zip_names()
    if set(rows) != expected:
        fail("checksum manifest does not match release ZIP set")
    for name, expected_digest in rows.items():
        path = DIST / name
        if path.is_file() and sha256(path) != expected_digest:
            fail(f"checksum mismatch: {name}")


def main() -> int:
    if not re.fullmatch(r"\d+\.\d+\.\d+", VERSION):
        fail(f"invalid VERSION: {VERSION!r}")
    validate_archives()
    validate_checksums()

    if ERRORS:
        print(f"FAIL: {len(ERRORS)} release validation error(s)")
        for error in ERRORS:
            print(f"- {error}")
        return 1
    print(f"PASS: {len(expected_zip_names())} ZIP files validated for AI Agent Tool {VERSION}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
