# ITHZ-MCP v0.1 product candidate

Build: `product-candidate-llm-intake.20260530.8`

This package is a production-test candidate for local deterministic project memory. It includes native `project.ithz` storage, memory-first MCP configs, host installer scripts, prompt/response summary memory, durable instruction memory, workflow profiles, Git merge driver support and shared-project smoke coverage.

Changes in this package:

- Uses one stable package artifact: `ithz_mcp.zip`.
- Moves build identity and source commit metadata to `VERSION.json`.
- Publishes the package hash in `SHA256SUMS.txt`.
- Handles systems without `git` in PATH without crashing `version` or `install-project`.
- Uses portable `.cmd` launchers instead of embedding the build machine's Python path.
- Reports native transport failures cleanly when `ithz-native.exe` is missing or blocked.

It does not replace Git, a production database, cloud sync, external host history, vector databases or every retrieval system.
