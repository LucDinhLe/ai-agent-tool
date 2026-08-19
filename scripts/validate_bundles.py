#!/usr/bin/env python3
"""Validate AI Agent Tool bundle structure without modifying files."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUNDLES = ROOT / "bundles"
VERSION = "2.0.0"

REQUIRED = {
    "codex": {
        "AGENTS.md",
        "AI-AGENT-TOOL.md",
        ".agents/skills/agents/SKILL.md",
        ".agents/skills/agents/agents/openai.yaml",
    },
    "claude-code": {
        "CLAUDE.md",
        "agents.md",
        "AI-AGENT-TOOL.md",
        ".claude/skills/agent-birth/SKILL.md",
    },
    "claude-cowork": {
        "agents.md",
        "COWORK-PROJECT-INSTRUCTIONS.txt",
        "AI-AGENT-TOOL.md",
        "cowork-skill/agent-birth/SKILL.md",
    },
    "gemini-cli": {
        "GEMINI.md",
        "AI-AGENT-TOOL.md",
        ".gemini/agents/agents.md",
        ".gemini/commands/ai-agent/init.toml",
        ".agents/skills/agent-birth/SKILL.md",
    },
    "github-copilot": {
        "AI-AGENT-TOOL.md",
        ".github/copilot-instructions.md",
        ".github/skills/agent-birth/SKILL.md",
        ".github/agents/ai-agent-tool.agent.md",
    },
    "openclaw": {
        "AGENTS.md",
        "BOOTSTRAP.md",
        "SOUL.md",
        "IDENTITY.md",
        "USER.md",
        "PROJECT.md",
        "TOOLS.md",
        "MEMORY.md",
        "memory/README.md",
        "AI-AGENT-TOOL.md",
        ".ai-agent-tool/BIRTH.md",
        ".ai-agent-tool/STATE.md",
        ".ai-agent-tool/MEMORY_POLICY.md",
        ".ai-agent-tool/GITIGNORE.fragment",
        ".agents/skills/agents/SKILL.md",
    },
}

PORTABLE_CORE = {
    ".ai-agent/.gitignore",
    ".ai-agent/VERSION",
    ".ai-agent/STATE.md",
    ".ai-agent/SOUL.md",
    ".ai-agent/WORKSPACE.md",
    ".ai-agent/MEMORY_POLICY.md",
    ".ai-agent/BIRTH.md",
    ".ai-agent/templates/private/USER.md",
    ".ai-agent/templates/private/TOOLS.md",
    ".ai-agent/templates/private/MEMORY.md",
    ".ai-agent/templates/private/memory/DAILY.template.md",
}

ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        fail(f"not UTF-8: {path.relative_to(ROOT)} ({exc})")
        return ""


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = read_text(path)
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(f"missing YAML frontmatter: {path.relative_to(ROOT)}")
        return {}
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.startswith((" ", "\t")):
            continue
        key, separator, value = line.partition(":")
        if separator:
            values[key.strip()] = value.strip().strip('"\'')
    return values


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_files() -> None:
    for name, required in REQUIRED.items():
        bundle = BUNDLES / name
        if not bundle.is_dir():
            fail(f"missing bundle directory: bundles/{name}")
            continue
        expected = set(required)
        if name != "openclaw":
            expected |= PORTABLE_CORE
        for relative in sorted(expected):
            if not (bundle / relative).is_file():
                fail(f"missing: bundles/{name}/{relative}")

        if (bundle / ".gitignore").exists():
            fail(f"root .gitignore would collide with target project: bundles/{name}")

    for path in BUNDLES.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".txt", ".toml", ".yaml"}:
            text = read_text(path)
            if "[TODO" in text or "TODO:" in text:
                fail(f"unresolved TODO: {path.relative_to(ROOT)}")


def validate_versions_and_state() -> None:
    for name in REQUIRED:
        version_path = (
            BUNDLES / name / (".ai-agent-tool/VERSION" if name == "openclaw" else ".ai-agent/VERSION")
        )
        if read_text(version_path).strip() != VERSION:
            fail(f"wrong version in bundles/{name}")

        state_path = (
            BUNDLES / name / (".ai-agent-tool/STATE.md" if name == "openclaw" else ".ai-agent/STATE.md")
        )
        state = read_text(state_path)
        if f"platform: {name}" not in state:
            fail(f"wrong platform state in bundles/{name}")
        if "status: uninitialized" not in state:
            fail(f"template state must be uninitialized in bundles/{name}")


def validate_skills() -> None:
    skill_paths = list(BUNDLES.rglob("SKILL.md"))
    if len(skill_paths) != 6:
        fail(f"expected 6 skills, found {len(skill_paths)}")
    for path in skill_paths:
        metadata = parse_frontmatter(path)
        if set(metadata) != {"name", "description"}:
            fail(f"skill frontmatter must contain only name and description: {path.relative_to(ROOT)}")
        name = metadata.get("name", "")
        if not re.fullmatch(r"[a-z0-9-]{1,63}", name):
            fail(f"invalid skill name {name!r}: {path.relative_to(ROOT)}")
        if len(metadata.get("description", "")) < 40:
            fail(f"skill description too short: {path.relative_to(ROOT)}")


def validate_invocations() -> None:
    checks = {
        "codex/AGENTS.md": ("@agents", "$agents"),
        "claude-code/CLAUDE.md": ("@agents.md", "/agent-birth"),
        "claude-cowork/COWORK-PROJECT-INSTRUCTIONS.txt": ("@agents",),
        "gemini-cli/.gemini/agents/agents.md": ("name: agents",),
        "gemini-cli/.gemini/commands/ai-agent/init.toml": ("prompt =",),
        "github-copilot/.github/copilot-instructions.md": ("@agents", "/agent-birth"),
        "openclaw/AGENTS.md": ("@agents", "/skill agents", "$agents"),
    }
    for relative, needles in checks.items():
        text = read_text(BUNDLES / relative)
        for needle in needles:
            if needle not in text:
                fail(f"missing invocation {needle!r}: bundles/{relative}")

    if len(read_text(BUNDLES / "claude-code/CLAUDE.md").splitlines()) >= 200:
        fail("Claude Code CLAUDE.md must remain under 200 lines")


def validate_imports() -> None:
    for relative in ("claude-code/CLAUDE.md", "gemini-cli/GEMINI.md"):
        path = BUNDLES / relative
        for line in read_text(path).splitlines():
            value = line.strip()
            if not value.startswith("@."):
                continue
            imported = value[1:]
            if not (path.parent / imported).resolve().is_file():
                fail(f"broken import {value}: bundles/{relative}")


def validate_common_core() -> None:
    names = ["codex", "claude-code", "claude-cowork", "gemini-cli", "github-copilot"]
    identical = [
        ".ai-agent/BIRTH.md",
        ".ai-agent/MEMORY_POLICY.md",
        ".ai-agent/WORKSPACE.md",
        ".ai-agent/templates/private/USER.md",
        ".ai-agent/templates/private/TOOLS.md",
        ".ai-agent/templates/private/MEMORY.md",
        ".ai-agent/templates/private/memory/DAILY.template.md",
    ]
    for relative in identical:
        hashes = {sha256(BUNDLES / name / relative) for name in names}
        if len(hashes) != 1:
            fail(f"portable core drift: {relative}")
    for name in names:
        ignore = read_text(BUNDLES / name / ".ai-agent/.gitignore").splitlines()
        if "/private/" not in ignore:
            fail(f"private memory not ignored: bundles/{name}")


def validate_git_privacy() -> None:
    try:
        result = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return
    for tracked in result.stdout.splitlines():
        normalized = tracked.replace("\\", "/")
        if not (ROOT / normalized).exists():
            continue
        if "/.ai-agent/private/" in normalized:
            fail(f"private portable memory is tracked: {normalized}")
        if "/private.example/" in normalized:
            fail(f"obsolete private.example path is tracked: {normalized}")


def main() -> int:
    validate_files()
    validate_versions_and_state()
    validate_skills()
    validate_invocations()
    validate_imports()
    validate_common_core()
    validate_git_privacy()

    if ERRORS:
        print(f"FAIL: {len(ERRORS)} validation error(s)")
        for error in ERRORS:
            print(f"- {error}")
        return 1
    print(f"PASS: {len(REQUIRED)} standalone bundles validated for AI Agent Tool {VERSION}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
