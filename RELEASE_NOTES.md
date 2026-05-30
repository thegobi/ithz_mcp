# ITHZ-MCP v0.1 product candidate

Build: `product-candidate-agent-intake.20260530.3`

This package is a production-test candidate for local deterministic project memory. It includes native `project.ithz` storage, memory-first MCP configs, host installer scripts, prompt/response summary memory, durable instruction memory, workflow profiles, Git merge driver support and shared-project smoke coverage.

This build adds first-install agent intake. `install-project --agent-intake auto` uses Codex CLI in read-only mode when available to store sanitized project summary, workflow, decision, gate and risk memory. If Codex CLI is not available, `ithz_mcp.md` asks the installing host agent to perform manual intake.

Normal `project.ithz` archives store memory/index layers, not a backup copy of the source tree.

Reinstalling into a project with an existing safe `project.ithz` reuses it and skips first-install agent intake and workflow re-adoption by default.

It does not replace Git, a production database, cloud sync, external host history, vector databases or every retrieval system.
