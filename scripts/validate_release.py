#!/usr/bin/env python3
"""Validate built one-folder AI Agent Tool archives without extracting them."""

from __future__ import annotations

import hashlib
import re
import stat
import sys
import zipfile
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

PLATFORMS = {
    "codex": {
        "archive": "AI-Agent-Tool-Codex.zip",
        "root": ".agents",
        "required": {
            ".agents/skills/ai-agent-tool/SKILL.md",
            ".agents/skills/ai-agent-tool/references/BOOTSTRAP.md",
            ".agents/skills/ai-agent-tool/assets/runtime/.ai-agent/VERSION",
        },
    },
    "claude-code": {
        "archive": "AI-Agent-Tool-Claude-Code.zip",
        "root": ".claude",
        "required": {
            ".claude/agents/ai-agent-tool.md",
            ".claude/rules/ai-agent-tool.md",
            ".claude/skills/agent-birth/SKILL.md",
            ".claude/skills/agent-birth/assets/runtime/.ai-agent/VERSION",
        },
    },
    "claude-cowork": {
        "archive": "AI-Agent-Tool-Claude-Cowork.zip",
        "root": "AI-Agent-Tool",
        "required": {
            "AI-Agent-Tool/START-HERE.md",
            "AI-Agent-Tool/COWORK-PROJECT-INSTRUCTIONS.txt",
            "AI-Agent-Tool/skill/agent-birth/SKILL.md",
            "AI-Agent-Tool/skill/agent-birth/assets/runtime/.ai-agent/VERSION",
        },
    },
    "gemini-cli": {
        "archive": "AI-Agent-Tool-Gemini-CLI.zip",
        "root": ".gemini",
        "required": {
            ".gemini/agents/ai-agent-tool.md",
            ".gemini/commands/agent-birth.toml",
            ".gemini/skills/agent-birth/SKILL.md",
            ".gemini/skills/agent-birth/assets/runtime/.ai-agent/VERSION",
        },
    },
    "github-copilot": {
        "archive": "AI-Agent-Tool-GitHub-Copilot.zip",
        "root": ".github",
        "required": {
            ".github/agents/ai-agent-tool.agent.md",
            ".github/instructions/ai-agent-tool.instructions.md",
            ".github/skills/agent-birth/SKILL.md",
            ".github/skills/agent-birth/assets/entry/AGENTS.md",
            ".github/skills/agent-birth/assets/runtime/.ai-agent/VERSION",
        },
    },
    "openclaw": {
        "archive": "AI-Agent-Tool-OpenClaw.zip",
        "root": "skills",
        "required": {
            "skills/agents/SKILL.md",
            "skills/agents/references/BOOTSTRAP.md",
            "skills/agents/assets/runtime/.ai-agent-tool/.gitignore",
            "skills/agents/assets/runtime/.ai-agent-tool/templates/private/USER.md",
            "skills/agents/assets/runtime/.ai-agent-tool/templates/private/MEMORY.md",
            "skills/agents/assets/runtime/.ai-agent-tool/VERSION",
            "skills/agents/assets/native/AGENTS.md",
        },
    },
}

COWORK_SKILL_ARCHIVE = "AI-Agent-Tool-Claude-Cowork-Skill.zip"
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expected_zip_names() -> set[str]:
    return {spec["archive"] for spec in PLATFORMS.values()} | {COWORK_SKILL_ARCHIVE}


def validate_safe_entries(archive_name: str, infos: list[zipfile.ZipInfo]) -> None:
    names = [info.filename for info in infos if not info.is_dir()]
    if len(names) != len(set(names)):
        fail(f"duplicate ZIP entry: {archive_name}")

    for info in infos:
        name = info.filename
        if info.is_dir():
            continue
        path = PurePosixPath(name)
        normalized = f"/{name.lower()}"
        file_type = stat.S_IFMT(info.external_attr >> 16)
        if file_type == stat.S_IFLNK:
            fail(f"symbolic link not allowed in {archive_name}: {name}")
        if "\\" in name or name.startswith("/") or re.match(r"^[a-zA-Z]:", name):
            fail(f"unsafe absolute or Windows path in {archive_name}: {name}")
        if ".." in path.parts:
            fail(f"path traversal in {archive_name}: {name}")
        if "/.ai-agent/private/" in normalized or "/.ai-agent-tool/private/" in normalized or "/private.example/" in normalized:
            fail(f"private memory included in {archive_name}: {name}")
        if "/tests/.tmp/" in normalized or path.name.lower() == ".env":
            fail(f"private or temporary file included in {archive_name}: {name}")


def read_archive(path: Path) -> set[str]:
    try:
        with zipfile.ZipFile(path) as archive:
            infos = archive.infolist()
            validate_safe_entries(path.name, infos)
            corrupt = archive.testzip()
            if corrupt:
                fail(f"CRC failure in {path.name}: {corrupt}")
            return {info.filename for info in infos if not info.is_dir()}
    except (OSError, zipfile.BadZipFile) as exc:
        fail(f"cannot read {path.name}: {exc}")
        return set()


def read_archive_text(path: Path, member: str) -> str:
    try:
        with zipfile.ZipFile(path) as archive:
            return archive.read(member).decode("utf-8")
    except (OSError, KeyError, UnicodeDecodeError, zipfile.BadZipFile) as exc:
        fail(f"cannot read {member} from {path.name}: {exc}")
        return ""


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

    archives = {
        name: read_archive(DIST / name)
        for name in sorted(expected)
        if (DIST / name).is_file()
    }

    for platform, spec in PLATFORMS.items():
        archive_name = spec["archive"]
        names = archives.get(archive_name, set())
        require_entries(archive_name, names, set(spec["required"]))
        roots = {PurePosixPath(name).parts[0] for name in names}
        if roots != {spec["root"]}:
            fail(
                f"{archive_name} must contain exactly one install folder "
                f"{spec['root']!r}, found {sorted(roots)}"
            )

    cowork_skill = archives.get(COWORK_SKILL_ARCHIVE, set())
    require_entries(
        COWORK_SKILL_ARCHIVE,
        cowork_skill,
        {
            "agent-birth/SKILL.md",
            "agent-birth/agents/openai.yaml",
            "agent-birth/references/BOOTSTRAP.md",
            "agent-birth/assets/runtime/.ai-agent/VERSION",
        },
    )
    cowork_roots = {PurePosixPath(name).parts[0] for name in cowork_skill}
    if cowork_roots != {"agent-birth"}:
        fail(
            f"{COWORK_SKILL_ARCHIVE} must contain the single skill folder "
            f"'agent-birth', found {sorted(cowork_roots)}"
        )

    cowork_skill_text = read_archive_text(
        DIST / COWORK_SKILL_ARCHIVE, "agent-birth/SKILL.md"
    )
    description_match = re.search(r"^description:\s*(.+)$", cowork_skill_text, re.MULTILINE)
    if not description_match or len(description_match.group(1).strip().strip('"\'')) > 200:
        fail("Cowork uploaded skill description must be present and at most 200 characters")

    openclaw_names = archives.get(PLATFORMS["openclaw"]["archive"], set())
    for forbidden in (
        "skills/agents/assets/native/USER.md",
        "skills/agents/assets/native/MEMORY.md",
        "skills/agents/assets/runtime/.ai-agent-tool/GITIGNORE.fragment",
    ):
        if forbidden in openclaw_names:
            fail(f"unsafe or obsolete OpenClaw payload entry: {forbidden}")

    for archive_name in sorted(expected):
        path = DIST / archive_name
        if not path.is_file():
            continue
        try:
            with zipfile.ZipFile(path) as archive:
                for info in archive.infolist():
                    if info.is_dir() or Path(info.filename).suffix.lower() not in {".md", ".txt", ".toml", ".yaml"}:
                        continue
                    text = archive.read(info).decode("utf-8")
                    if "/ai-agent:init" in text:
                        fail(f"legacy Gemini invocation in {archive_name}: {info.filename}")
        except (OSError, UnicodeDecodeError, zipfile.BadZipFile) as exc:
            fail(f"cannot inspect text payload in {archive_name}: {exc}")


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
    print(f"PASS: {len(expected_zip_names())} one-folder ZIP files validated for AI Agent Tool {VERSION}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
