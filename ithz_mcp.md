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
9. If the user gives a durable project instruction, store it as typed memory in `project.ithz` with the write-enabled durable instruction tools.
10. After installation, report exactly what was created, reused, and configured.

## Package Source

Trusted package repository:

```text
https://github.com/thegobi/ithz_mcp.git
```

Package file:

```text
ithz_mcp.zip
```

Raw package URL:

```text
https://github.com/thegobi/ithz_mcp/raw/main/ithz_mcp.zip
```

If this file is distributed inside an ITHZ-MCP package, use that package directly.

If this file was copied into a project, clone the trusted repository or ask the user for the local package path. Do not guess a random GitHub repository.

For a private repository, use Git/Git Credential Manager or the host's configured GitHub authentication.

Do not keep the downloaded package inside the target project. Install or extract the runtime into a user-local cache, then run the installer from there. Project-local `.ithz-install` is only temporary scratch plus an installation log.

```powershell
$RuntimeRoot = Join-Path $env:LOCALAPPDATA "ITHZ-MCP\packages\ithz_mcp"
New-Item -ItemType Directory -Force -Path (Split-Path $RuntimeRoot) | Out-Null
$RepoRoot = "$RuntimeRoot-repo"
if (Test-Path $RepoRoot) { Remove-Item -Recurse -Force $RepoRoot }
git clone https://github.com/thegobi/ithz_mcp.git $RepoRoot
if (Test-Path $RuntimeRoot) { Remove-Item -Recurse -Force $RuntimeRoot }
Expand-Archive "$RepoRoot\ithz_mcp.zip" $RuntimeRoot -Force
python -m ithz_mcp version
```

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

Installer scratch files are written under `.ithz-install/tmp/` and are removed after a successful install unless `--keep-install-artifacts` is explicitly used. After a normal successful install, `.ithz-install/` should contain only `install.log`.

On first install, `install-project` also runs first project intake:

```powershell
python -m ithz_mcp install-project --apply --import-agent-history --agent-intake auto
```

`--agent-intake auto` first builds a bounded deterministic repo dossier: project scale, directory summary, ranked candidate files, and short redacted excerpts. Codex CLI then runs in read-only mode when `codex` is available and is prompted to select important files/sections from that dossier. It records only sanitized project summary, workflow rules, decisions, gates, risks, candidate files, next steps, and evidence gaps into `project.ithz`. It must not store secrets and must not store a source snapshot unless explicitly requested for diagnostics.

If Codex CLI is not available, or the installer reports `manual_host_intake_required=true`, the installing agent must complete host-side intake in this thread before continuing normal work:

1. Read `project.md`.
2. Ask ITHZ-MCP for status and an archive context pack.
3. Inspect only the small set of bootstrap/project docs needed to understand workflow, deploy, tests, gates, risks, and decisions.
4. Store durable findings explicitly:

```powershell
python -m ithz_mcp ingest-user-instruction --project . --profile <user-or-team-profile> --text "<short durable workflow/decision/gate/risk summary>"
```

or use the typed commands:

```powershell
python -m ithz_mcp record-workflow-rule --project . --profile <user-or-team-profile> --text "<durable workflow rule>"
python -m ithz_mcp record-project-decision --project . --profile <user-or-team-profile> --text "<project decision>"
python -m ithz_mcp record-gate-rule --project . --profile <user-or-team-profile> --text "<required validation gate>"
python -m ithz_mcp record-risk-rule --project . --profile <user-or-team-profile> --text "<must-not-break or safety rule>"
```

5. Report whether manual host intake was completed. Do not pretend the project was semantically analyzed if only deterministic path/index data was recorded.

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

If the user gives a lasting workflow rule such as "after each task, run tests, commit and deploy through SSH", do not leave it only in the chat. Store it explicitly:

```powershell
python -m ithz_mcp record-workflow-rule --project . --profile <user-or-team-profile> --text "<durable workflow rule>"
python -m ithz_mcp record-gate-rule --project . --profile <user-or-team-profile> --text "<required validation gate>"
python -m ithz_mcp record-risk-rule --project . --profile <user-or-team-profile> --text "<must-not-break or secret-safety rule>"
```

Or ingest a short instruction block deterministically:

```powershell
python -m ithz_mcp ingest-user-instruction --project . --profile <user-or-team-profile> --text "<user instruction block>"
```

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
