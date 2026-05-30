# ITHZ-MCP package

This repository carries the installable ITHZ-MCP package artifact, not the development source tree.

Use it like this:

1. Copy `ithz_mcp.md` into the target project.
2. Ask the local coding agent: `See ithz_mcp.md and install`.
3. The agent downloads or clones this package repository, expands `ithz_mcp-v0.1-product-candidate-20260530.2.zip` or the latest alias `ithz_mcp-v0.1-product-candidate.zip`, runs smoke checks, initializes the current project, reuses existing `project.ithz` if present, and configures local MCP/Git-driver support.
4. If the user gives durable workflow, decision, gate or risk instructions, the write-enabled MCP profile stores them as typed memory in `project.ithz`.

Repository:

```text
https://github.com/thegobi/ithz_mcp.git
```

Direct package URL:

```text
https://github.com/thegobi/ithz_mcp/raw/main/ithz_mcp-v0.1-product-candidate.zip
```

Versioned package URL:

```text
https://github.com/thegobi/ithz_mcp/raw/main/ithz_mcp-v0.1-product-candidate-20260530.2.zip
```

Package file:

```text
ithz_mcp-v0.1-product-candidate.zip
ithz_mcp-v0.1-product-candidate-20260530.2.zip
```

Build `product-candidate-agent-intake.20260530.2` adds first-install agent intake. If Codex CLI is available, it performs a read-only project analysis and stores sanitized workflow/decision/gate/risk memory in `project.ithz`. If Codex CLI is missing, `ithz_mcp.md` instructs the installing host agent to finish intake manually.

Normal `project.ithz` files do not store source snapshots by default; they store memory/index layers. Use source snapshots only as explicit diagnostics.

ITHZ-MCP does not replace Git, a production database, cloud sync, host chat history, or every retrieval system.
