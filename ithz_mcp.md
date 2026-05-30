# ITHZ-MCP Bootstrap Installer

Use this file when you want an AI coding agent to install ITHZ-MCP into the current project.

Product rule:

```text
Markdown is the bootstrap. ITHZ is the memory zone.
Git shares code history. ITHZ-MCP shares agent work memory.
```

ITHZ-MCP does not replace Git, a production database, cloud sync, the host chat history, or every retrieval system.

## Agent Instructions

If you are Codex, Claude Code, Cursor, Antigravity, or another local coding agent:

1. Treat the current directory as the target project root.
2. Do not scan the whole project blindly before installing or checking ITHZ-MCP.
3. If `project.ithz` already exists, verify and reuse it. Do not replace it.
4. If `project.md` already exists, preserve it. If it is missing, create a minimal bootstrap.
5. Do not index or store secrets such as `.env`, `*.pem`, `*.key`, credential files, private keys, API tokens, or password-like values.
6. Do not run `git add`, `git commit`, `git push`, `git reset`, or `git checkout` automatically.
7. If Git is present, configure the ITHZ diff/merge driver so `project.ithz` can be reviewed and semantically merged.
8. If local agent history is available, import only redacted summaries and append them to the existing `project.ithz`.
9. After installation, report exactly what was created, reused, and configured.

## Package Source

Preferred installation source:

```text
https://github.com/thegobi/ithz_mcp/raw/main/ithz_mcp-v0.1-product-candidate.zip
```

If this file is distributed inside an ITHZ-MCP package, use that package directly.

If this file was copied into a project and no trusted package URL or local package path is available, ask the user for the package location. Do not guess a random GitHub repository.

## Install From A Package Folder

Open a terminal in the package folder and run:

```powershell
python -m ithz_mcp version
python -m ithz_mcp self-test --verbose
```

Then install into the target project:

```powershell
cd <target-project>
python -m ithz_mcp install-project --apply --import-agent-history
```

For a normal first install, this creates or validates:

```text
project.md
project.ithz
.gitattributes
.gitignore
```

Installer scratch files are written under `.ithz-install/tmp/` and are removed after a successful install unless `--keep-install-artifacts` is explicitly used.

## Existing Team Project

If the project already has `project.ithz` from Git:

1. Verify it with ITHZ-MCP.
2. Reuse the existing archive.
3. Append this user's workflow profile and redacted local prompt summaries.
4. Preserve existing context commits, decisions, gates, prompt summaries, refs, indexes, and snapshots.
5. Do not rebuild the archive from scratch unless the user explicitly asks for a repair/rebuild operation.

## Host Setup

After project installation, configure the local host if requested:

```powershell
python -m ithz_mcp mcp-config-template --project . --client codex --out .ithz-install/tmp/codex_mcp_config.json
python -m ithz_mcp mcp-config-validate --config .ithz-install/tmp/codex_mcp_config.json
```

Use the write-enabled host profile only for explicit end-of-task checkpointing. The read-only profile must remain safe and must not expose write tools.

## First Agent Run After Install

Use this startup sequence:

1. Read `project.md`.
2. Call ITHZ-MCP status.
3. Check the active memory zone.
4. Request a context pack for the task.
5. Inspect only candidate files and evidence gaps returned by the pack.
6. After the task, write a sanitized checkpoint if the write-enabled profile is active.

## Success Criteria

Installation is successful only if:

- `project.md` exists.
- `project.ithz` exists and safe verify passes.
- secrets were not indexed.
- existing `project.ithz` was reused if present.
- Git driver configuration was installed or reported as not applicable.
- no Git commit was made automatically.
- no cloud sync was added.
- no Git replacement or general token-saving claim was added.
