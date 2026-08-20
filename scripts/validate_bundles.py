#!/usr/bin/env python3
"""Validate one-folder AI Agent Tool source bundles without modifying files."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

BUNDLES = {
    "codex": {
        "root": ".agents",
        "skill": ".agents/skills/ai-agent-tool/SKILL.md",
        "payload": ".agents/skills/ai-agent-tool/assets/runtime/.ai-agent",
        "required": {
            ".agents/skills/ai-agent-tool/SKILL.md",
            ".agents/skills/ai-agent-tool/agents/openai.yaml",
            ".agents/skills/ai-agent-tool/references/BOOTSTRAP.md",
            ".agents/skills/ai-agent-tool/references/INSTALL.md",
            ".agents/skills/ai-agent-tool/assets/entry/AGENTS.md",
        },
    },
    "claude-code": {
        "root": ".claude",
        "skill": ".claude/skills/agent-birth/SKILL.md",
        "payload": ".claude/skills/agent-birth/assets/runtime/.ai-agent",
        "required": {
            ".claude/agents/ai-agent-tool.md",
            ".claude/rules/ai-agent-tool.md",
            ".claude/skills/agent-birth/SKILL.md",
            ".claude/skills/agent-birth/references/BOOTSTRAP.md",
            ".claude/skills/agent-birth/references/INSTALL.md",
        },
    },
    "claude-cowork": {
        "root": "AI-Agent-Tool",
        "skill": "AI-Agent-Tool/skill/agent-birth/SKILL.md",
        "payload": "AI-Agent-Tool/skill/agent-birth/assets/runtime/.ai-agent",
        "required": {
            "AI-Agent-Tool/START-HERE.md",
            "AI-Agent-Tool/agents.md",
            "AI-Agent-Tool/COWORK-PROJECT-INSTRUCTIONS.txt",
            "AI-Agent-Tool/skill/agent-birth/SKILL.md",
            "AI-Agent-Tool/skill/agent-birth/references/BOOTSTRAP.md",
        },
    },
    "gemini-cli": {
        "root": ".gemini",
        "skill": ".gemini/skills/agent-birth/SKILL.md",
        "payload": ".gemini/skills/agent-birth/assets/runtime/.ai-agent",
        "required": {
            ".gemini/agents/ai-agent-tool.md",
            ".gemini/commands/agent-birth.toml",
            ".gemini/skills/agent-birth/SKILL.md",
            ".gemini/skills/agent-birth/references/BOOTSTRAP.md",
            ".gemini/skills/agent-birth/references/INSTALL.md",
            ".gemini/skills/agent-birth/assets/entry/GEMINI.md",
        },
    },
    "github-copilot": {
        "root": ".github",
        "skill": ".github/skills/agent-birth/SKILL.md",
        "payload": ".github/skills/agent-birth/assets/runtime/.ai-agent",
        "required": {
            ".github/agents/ai-agent-tool.agent.md",
            ".github/instructions/ai-agent-tool.instructions.md",
            ".github/skills/agent-birth/SKILL.md",
            ".github/skills/agent-birth/references/BOOTSTRAP.md",
            ".github/skills/agent-birth/references/INSTALL.md",
            ".github/skills/agent-birth/assets/entry/AGENTS.md",
        },
    },
    "openclaw": {
        "root": "skills",
        "skill": "skills/agents/SKILL.md",
        "payload": "skills/agents/assets/runtime/.ai-agent-tool",
        "required": {
            "skills/agents/SKILL.md",
            "skills/agents/references/BOOTSTRAP.md",
            "skills/agents/references/INSTALL.md",
            "skills/agents/assets/native/AGENTS.md",
            "skills/agents/assets/native/SOUL.md",
            "skills/agents/assets/native/IDENTITY.md",
            "skills/agents/assets/native/PROJECT.md",
        },
    },
}

PORTABLE_CORE = {
    ".gitignore",
    "BIRTH.md",
    "MEMORY_POLICY.md",
    "SOUL.md",
    "STATE.md",
    "VERSION",
    "WORKSPACE.md",
    "templates/private/USER.md",
    "templates/private/TOOLS.md",
    "templates/private/MEMORY.md",
    "templates/private/memory/DAILY.template.md",
}

ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        fail(f"cannot read UTF-8 file {path.relative_to(ROOT)}: {exc}")
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


def release_source_files(platform: str) -> list[str]:
    try:
        result = subprocess.run(
            [
                "git",
                "-C",
                str(ROOT),
                "ls-files",
                "--cached",
                "--others",
                "--exclude-standard",
                "--",
                f"{platform}/",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        fail(f"cannot enumerate release source for {platform}: {exc}")
        return []
    files: list[str] = []
    prefix = f"{platform}/"
    for tracked in result.stdout.splitlines():
        normalized = tracked.replace("\\", "/")
        path = ROOT / normalized
        if normalized.startswith(prefix) and path.is_file():
            files.append(normalized[len(prefix) :])
    return files


def validate_one_folder_layout() -> None:
    for platform, spec in BUNDLES.items():
        bundle = ROOT / platform
        if not bundle.is_dir():
            fail(f"missing platform directory: {platform}")
            continue

        files = release_source_files(platform)
        if not files:
            fail(f"empty release source: {platform}")
            continue
        roots = {Path(relative).parts[0] for relative in files}
        if roots != {spec["root"]}:
            fail(f"{platform} must install exactly one folder {spec['root']!r}, found {sorted(roots)}")

        required = set(spec["required"])
        if platform != "openclaw":
            required |= {f"{spec['payload']}/{relative}" for relative in PORTABLE_CORE}
        else:
            required |= {
                f"{spec['payload']}/BIRTH.md",
                f"{spec['payload']}/.gitignore",
                f"{spec['payload']}/MEMORY_POLICY.md",
                f"{spec['payload']}/STATE.md",
                f"{spec['payload']}/VERSION",
                f"{spec['payload']}/templates/private/USER.md",
                f"{spec['payload']}/templates/private/MEMORY.md",
                f"{spec['payload']}/templates/private/memory/DAILY.template.md",
            }
        for relative in sorted(required):
            if not (bundle / relative).is_file():
                fail(f"missing: {platform}/{relative}")

        for relative in files:
            path = bundle / relative
            if path.suffix.lower() in {".md", ".txt", ".toml", ".yaml"}:
                text = read_text(path)
                if "[TODO" in text or "TODO:" in text:
                    fail(f"unresolved TODO: {path.relative_to(ROOT)}")


def validate_versions_and_state() -> None:
    if not re.fullmatch(r"\d+\.\d+\.\d+", VERSION):
        fail(f"invalid root VERSION: {VERSION!r}")

    for platform, spec in BUNDLES.items():
        payload = ROOT / platform / spec["payload"]
        if read_text(payload / "VERSION").strip() != VERSION:
            fail(f"wrong payload version in {platform}")
        state = read_text(payload / "STATE.md")
        if f"platform: {platform}" not in state:
            fail(f"wrong platform state in {platform}")
        if "status: uninitialized" not in state:
            fail(f"template state must be uninitialized in {platform}")


def validate_skills() -> None:
    skill_paths = [ROOT / platform / spec["skill"] for platform, spec in BUNDLES.items()]
    if len(skill_paths) != 6:
        fail(f"expected 6 skills, found {len(skill_paths)}")
    for path in skill_paths:
        metadata = parse_frontmatter(path)
        relative = path.relative_to(ROOT).as_posix()
        expected_keys = {"name", "description"}
        if set(metadata) != expected_keys:
            fail(f"unexpected skill frontmatter keys: {relative}: {sorted(metadata)}")
        name = metadata.get("name", "")
        if not re.fullmatch(r"[a-z0-9-]{1,63}", name):
            fail(f"invalid skill name {name!r}: {relative}")
        description = metadata.get("description", "")
        if len(description) < 40:
            fail(f"skill description too short: {relative}")
        if relative.startswith("openclaw/"):
            if len(description) > 160:
                fail("OpenClaw skill description must be at most 160 characters")
        if relative.startswith("claude-cowork/") and len(description) > 200:
            fail("Claude Cowork upload skill description must be at most 200 characters")


def validate_invocations() -> None:
    checks = {
        "codex/.agents/skills/ai-agent-tool/SKILL.md": ("@agents", "$agents"),
        "claude-code/.claude/rules/ai-agent-tool.md": ("@agents", "@agent-agents", "/agent-birth", "/agents"),
        "claude-cowork/AI-Agent-Tool/COWORK-PROJECT-INSTRUCTIONS.txt": ("@agents", "AI-Agent-Tool/skill/agent-birth/SKILL.md"),
        "gemini-cli/.gemini/agents/ai-agent-tool.md": ("name: agents", "agent-birth/SKILL.md", "grep_search"),
        "gemini-cli/.gemini/commands/agent-birth.toml": ("prompt =", "agent-birth/SKILL.md"),
        "github-copilot/.github/instructions/ai-agent-tool.instructions.md": ("@agents", "/agent-birth", "applyTo: \"**\""),
        "openclaw/skills/agents/SKILL.md": ("$agents", "/skill agents", "`/agents`"),
    }
    for relative, needles in checks.items():
        text = read_text(ROOT / relative)
        for needle in needles:
            if needle not in text:
                fail(f"missing invocation {needle!r}: {relative}")

    for platform in BUNDLES:
        for relative in release_source_files(platform):
            path = ROOT / platform / relative
            if path.suffix.lower() in {".md", ".txt", ".toml", ".yaml"} and "/ai-agent:init" in read_text(path):
                fail(f"legacy Gemini invocation in current bundle: {platform}/{relative}")

    claude_rule = ROOT / "claude-code/.claude/rules/ai-agent-tool.md"
    if len(read_text(claude_rule).splitlines()) >= 200:
        fail("Claude Code project rule must remain under 200 lines")


def validate_common_core() -> None:
    platforms = ["codex", "claude-code", "claude-cowork", "gemini-cli", "github-copilot"]
    identical = {
        "BIRTH.md",
        "MEMORY_POLICY.md",
        "WORKSPACE.md",
        "templates/private/USER.md",
        "templates/private/TOOLS.md",
        "templates/private/MEMORY.md",
        "templates/private/memory/DAILY.template.md",
    }
    for relative in identical:
        hashes = {
            sha256(ROOT / platform / BUNDLES[platform]["payload"] / relative)
            for platform in platforms
        }
        if len(hashes) != 1:
            fail(f"portable core drift: {relative}")
    for platform in platforms:
        payload = ROOT / platform / BUNDLES[platform]["payload"]
        ignore = read_text(payload / ".gitignore").splitlines()
        if "/private/" not in ignore:
            fail(f"private memory not ignored: {platform}")
        if (payload / "private").exists():
            fail(f"real private memory shipped in source payload: {platform}")


def validate_bootstrap_contracts() -> None:
    for platform, spec in BUNDLES.items():
        skill = read_text(ROOT / platform / spec["skill"])
        bootstrap = ROOT / platform / Path(spec["skill"]).parent / "references/BOOTSTRAP.md"
        if "BOOTSTRAP.md" not in skill or not bootstrap.is_file():
            fail(f"missing bootstrap routing in {platform}")
        bootstrap_text = read_text(bootstrap)
        for phrase in ("Never write outside", "meaningful content"):
            if phrase not in bootstrap_text:
                fail(f"bootstrap safety contract missing {phrase!r}: {platform}")

    codex_entry = read_text(ROOT / "codex/.agents/skills/ai-agent-tool/assets/entry/AGENTS.md")
    copilot_entry = read_text(ROOT / "github-copilot/.github/skills/agent-birth/assets/entry/AGENTS.md")
    gemini_entry = read_text(ROOT / "gemini-cli/.gemini/skills/agent-birth/assets/entry/GEMINI.md")
    openclaw_entry = read_text(ROOT / "openclaw/skills/agents/assets/native/AGENTS.md")
    for name, text in (("codex", codex_entry), ("github-copilot", copilot_entry), ("gemini-cli", gemini_entry), ("openclaw", openclaw_entry)):
        if "<!-- AI-AGENT-TOOL:START -->" not in text or "<!-- AI-AGENT-TOOL:END -->" not in text:
            fail(f"managed entry markers missing: {name}")

    openclaw_payload = ROOT / "openclaw" / BUNDLES["openclaw"]["payload"]
    if "/private/" not in read_text(openclaw_payload / ".gitignore").splitlines():
        fail("OpenClaw private runtime is not ignored")
    for unsafe_native in ("USER.md", "MEMORY.md"):
        if (ROOT / "openclaw/skills/agents/assets/native" / unsafe_native).exists():
            fail(f"OpenClaw must not ship private-looking root template: {unsafe_native}")


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
        if "/.ai-agent/private/" in normalized:
            fail(f"private portable memory is tracked: {normalized}")
        if "/private.example/" in normalized:
            fail(f"obsolete private.example path is tracked: {normalized}")
        if normalized.endswith("/.env"):
            fail(f"environment file is tracked in bundle source: {normalized}")


def main() -> int:
    for relative in ("VERSION", "README.md", "00-BAT-DAU-O-DAY.md"):
        if not (ROOT / relative).is_file():
            fail(f"missing root distribution file: {relative}")
    if (ROOT / "bundles").exists():
        fail("obsolete bundles/ wrapper still exists")

    validate_one_folder_layout()
    validate_versions_and_state()
    validate_skills()
    validate_invocations()
    validate_common_core()
    validate_bootstrap_contracts()
    validate_git_privacy()

    if ERRORS:
        print(f"FAIL: {len(ERRORS)} validation error(s)")
        for error in ERRORS:
            print(f"- {error}")
        return 1
    print(f"PASS: {len(BUNDLES)} one-folder bundles validated for AI Agent Tool {VERSION}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
