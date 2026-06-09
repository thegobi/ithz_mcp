# ITHZ Install Agent Playbook

Use this file as the one prompt target for an AI coding agent.

User prompt:

```text
See install_ithz.md and install ITHZ-MCP into this project.
```

If this file is not already present in the target project, use this shorter bootstrap prompt:

```text
Download the official ITHZ-MCP package from https://ithz.dev/download/, unzip it, find install_ithz.md inside it, and follow that file to install ITHZ-MCP into this current project. Do not invent steps and do not commit anything automatically.
```

## Non-Negotiable Defaults

1. The current directory is the target project root.
2. Do not scan the whole project blindly before installation.
3. Do not index secrets: `.env`, `*.pem`, `*.key`, credentials, private keys, API tokens or password-like values.
4. Do not run `git add`, `git commit`, `git push`, `git reset` or `git checkout` automatically.
5. If `project.ithz` already exists, verify and reuse it. Do not replace it.
6. If `project.md` exists, preserve it. If missing and native storage is available, create a minimal bootstrap.
7. Configure the ITHZ Git diff/merge driver when Git is present.
8. Ask the user only for dangerous or truly ambiguous operations.

## OS Decision Tree

### Windows

Install the full supported workflow when the Windows package is available:

- ITHZ-MCP runtime;
- native `project.ithz` storage through bundled AVX2/scalar `ithz-native.exe`;
- host MCP config;
- Git diff/merge driver;
- optional ITHZ Drive shell integration if the Drive package is present.

### macOS

First look for a compatible macOS `ithz-native` in this order:

1. `ITHZ_NATIVE_EXE`;
2. package-local `native/ithz-native`;
3. `$HOME/.local/share/ithz-mcp/native/ithz-native`;
4. an explicitly supplied local or CI-built macOS native package.

Do not assume that `ithz-native-preview-v0.1-alpha-rc2-macos-x86_64.zip` is a
public download from `ithz.dev`. If the user has not supplied that package, do
not try guessed URLs. Continue with the safe fallback below and report the
native-binary gap.

If the binary exists, validate it:

```sh
"$ITHZ_NATIVE_EXE" --version
"$ITHZ_NATIVE_EXE" --self-test
```

Then install host config with native archive storage:

```sh
ITHZ_NATIVE_EXE="$ITHZ_NATIVE_EXE" \
ITHZ_MCP_STORAGE_PROFILE=native-archive \
host_installers_macos/install_cursor_mcp.sh --project "$PWD" --apply
```

If no compatible macOS `ithz-native` binary is found, do not ask the user which option to pick. Continue with the safe official subset:

- Cursor/Codex/Claude/Antigravity MCP host config;
- `*.ithz` Git diff/merge driver;
- ITHZ Drive.app or open-as-temporary-folder fallback if present;
- a clear native-binary gap report.

Use legacy MCP storage for the host config in this partial mode. Do not create, overwrite or repack native `project.ithz` storage until `ITHZ_NATIVE_EXE` points to a compatible macOS `ithz-native` binary or the package ships one.

If an existing `project.ithz` was pulled from Git, preserve it and configure Git diff/merge support. Without native support, do not rewrite it.

### Linux

Install MCP host config and Git diff/merge driver. Use native `project.ithz` storage only when a compatible Linux `ithz-native` binary is present or built locally.

## Package Source

Trusted repository:

```text
https://github.com/thegobi/ithz_mcp.git
```

Trusted package file:

```text
ithz_mcp.zip
```

Raw package URL:

```text
https://github.com/thegobi/ithz_mcp/raw/main/ithz_mcp.zip
```

Do not guess another repository. For a private repository, use the host's configured Git/GitHub authentication.

Official download page:

```text
https://ithz.dev/download/
```

When installing from the public download page, download only the matching official package for the current OS, unzip it outside the target project or in a temporary installer directory, locate `install_ithz.md` in the package root, then continue from this file. Do not leave the downloaded ZIP or expanded runtime inside the project after a successful install unless the user explicitly asks for that.

## Install Command Shape

From the package folder, smoke test first:

```sh
python -m ithz_mcp version
python -m ithz_mcp self-test --verbose
```

Then from the target project:

```sh
python -m ithz_mcp install-project --apply --import-agent-history --agent-intake auto
```

On macOS without native storage, host installers may be used directly:

```sh
host_installers_macos/install_cursor_mcp.sh --project "$PWD" --apply
host_installers_macos/install_claude_code_mcp.sh --project "$PWD" --apply
host_installers_macos/install_codex_mcp.sh --project "$PWD" --apply
```

## Project Memory Intake

After installation, populate project memory in a bounded and redacted way:

1. Import available local prompts, agent history or prompt archives only through ITHZ-MCP redaction-aware import.
2. Inspect relevant project Markdown files such as workflow, roadmap, architecture, decisions, gates and README documents.
3. Store concise records in project memory: workflow rules, decisions, gates, risks, candidate files, next steps and evidence gaps.
4. Do not store raw secrets, raw credentials or private keys.
5. Do not store a full source snapshot unless the user explicitly asks for a diagnostic snapshot and the project is small enough.
6. For large repositories, use compact/large-repo mode and prefer curated docs plus high-signal file summaries.

If native `project.ithz` storage is available, these durable facts should end up in `project.ithz`. If native storage is not available on the current OS, install the MCP host config and report which memory writes are deferred or using legacy local storage.

## Verification And Cleanup

Run the short available smoke checks for the current package:

- MCP server/config validation;
- host-specific client smoke when available;
- Git driver status when Git is present;
- native archive safe verify when native storage is available.

After a successful install, clean temporary installer files. Project-local `.ithz-install/` should contain only an installation log unless the user explicitly asks to keep artifacts.

If a write-enabled ITHZ-MCP profile is active, create a sanitized auto checkpoint describing:

- what was installed;
- which host configs were written;
- whether native storage is available;
- what project memory was imported;
- which warnings or gaps remain.

## Success Report

At the end, report:

- what was created;
- what was reused;
- whether `project.ithz` exists and was verified or deferred;
- which MCP host configs were installed;
- whether Git diff/merge driver was configured;
- whether secrets were excluded;
- whether native support is available or missing;
- next exact command for the user.

ITHZ-MCP does not replace Git, a production database, cloud sync, the host chat history or every retrieval system.
