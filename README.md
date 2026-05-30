# ITHZ-MCP package

This repository carries the installable ITHZ-MCP package artifact, not the development source tree.

Use it like this:

1. Copy `ithz_mcp.md` into the target project.
2. Ask the local coding agent: `See ithz_mcp.md and install`.
3. The agent clones this private package repository, expands `ithz_mcp-v0.1-product-candidate.zip`, runs smoke checks, initializes the current project, reuses existing `project.ithz` if present, and configures local MCP/Git-driver support.
4. If the user gives durable workflow, decision, gate or risk instructions, the write-enabled MCP profile stores them as typed memory in `project.ithz`.

Trusted package repository:

```text
https://github.com/thegobi/ithz_mcp.git
```

Package file:

```text
ithz_mcp-v0.1-product-candidate.zip
```

The raw package URL requires GitHub access to this private repository:

```text
https://github.com/thegobi/ithz_mcp/raw/main/ithz_mcp-v0.1-product-candidate.zip
```

ITHZ-MCP does not replace Git, a production database, cloud sync, host chat history, or every retrieval system.
