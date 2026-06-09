# ITHZ-MCP v0.1 product candidate

Build: `product-candidate-llm-intake.20260530.8`

This package is a production-test candidate for local deterministic project memory. It includes native `project.ithz` storage, memory-first MCP configs, host installer scripts, prompt/response summary memory, durable instruction memory, workflow profiles, Git merge driver support and shared-project smoke coverage.

Changes in this package:

- Uses one stable package artifact: `ithz_mcp.zip`.
- Adds `ithz-mcp-macos.zip` for macOS stdio MCP host setup.
- Adds Ubuntu/Linux package artifacts: `ithz-mcp-ubuntu.tar.gz` and
  `ithz-mcp-ubuntu.deb`.
- Adds `ithz-native-macos-intel-build-kit.zip`, which contains the native
  source subset needed to build `ithz-native` on Mac Intel.
- Adds GitHub Actions workflow support for building the Mac Intel native
  package from the public build kit.
- Moves build identity and source commit metadata to `VERSION.json`.
- Publishes the package hash in `SHA256SUMS.txt`.
- Handles systems without `git` in PATH without crashing `version` or `install-project`.
- Uses portable `.cmd` launchers instead of embedding the build machine's Python path.
- Reports native transport failures cleanly when `ithz-native.exe` is missing or blocked.

The macOS MCP package works as a Python stdio MCP server. Native `project.ithz`
storage on macOS requires the Mac Intel `ithz-native` binary built from the
included build kit or supplied separately.

Ubuntu update: `install_ithz.md` is included in the tarball, user-local command
wrappers are generated as prefix scripts instead of broken symlinks, and the
Linux native build kit dynamically loads `libz.so.1` / `libz.so` for native
archive operations.

It does not replace Git, a production database, cloud sync, external host history, vector databases or every retrieval system.
