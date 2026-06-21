# ITHZ MCP

<!-- mcp-name: dev.ithz/ithz-mcp -->

[![PyPI](https://img.shields.io/pypi/v/ithz-mcp?label=PyPI)](https://pypi.org/project/ithz-mcp/)
[![MCP Registry](https://img.shields.io/badge/MCP%20Registry-dev.ithz%2Fithz--mcp-blue)](https://registry.modelcontextprotocol.io/v0.1/servers/dev.ithz%2Fithz-mcp/versions/latest)
[![GitHub Release](https://img.shields.io/github/v/release/thegobi/ithz_mcp?include_prereleases&label=GitHub%20release)](https://github.com/thegobi/ithz_mcp/releases/tag/v0.1.0a1)

Local-first deterministic project memory for AI coding agents and
MCP-compatible development workflows.

ITHZ MCP stores durable agent work memory in project-owned files: context packs,
decisions, gates, risks, reviewer notes, scoped claims and explicit checkpoints.
Git remains the code history and transport; ITHZ MCP keeps the operational
memory that helps agents resume work without depending only on hidden chat
history or repeated full-repo scans.

## Public Links

- Product page: https://ithz.dev/mcp/
- PyPI package: https://pypi.org/project/ithz-mcp/
- Official MCP Registry name: `dev.ithz/ithz-mcp`
- Official MCP Registry API:
  https://registry.modelcontextprotocol.io/v0.1/servers/dev.ithz%2Fithz-mcp/versions/latest
- Package repository: https://github.com/thegobi/ithz_mcp

## Install From PyPI

```sh
python -m pip install ithz-mcp
python -m ithz_mcp version
```

Minimal stdio MCP configuration:

```json
{
  "mcpServers": {
    "ithz_mcp": {
      "command": "python",
      "args": [
        "-m",
        "ithz_mcp",
        "mcp-server",
        "--project",
        "/path/to/project",
        "--mode",
        "read-only",
        "--protocol",
        "direct",
        "--storage-profile",
        "native-archive"
      ]
    }
  }
}
```

Use a write-enabled profile only when your host and workflow explicitly allow
the agent to append sanitized task checkpoints into `project.ithz`.

## What It Is

ITHZ MCP is a local project-memory layer for AI-assisted development. It is
designed for agents and developers who want deterministic, auditable handoff
state next to the project:

- context packs for onboarding an agent to a repo or task
- durable decisions, gates, risks and next steps
- reviewer notes and scoped claim ledgers
- end-of-task checkpoints for future agents
- local-first operation through project-owned memory files
- MCP stdio integration for compatible coding-agent hosts

## What It Is Not

ITHZ MCP does not replace Git, a production database, cloud sync, a source-code
backup, a vector database, or every retrieval system. It complements these tools
by keeping durable project memory explicit and inspectable.

## Distribution Artifacts

This repository carries public package artifacts and metadata, not the full
development source tree.

Direct artifact URLs:

```text
https://github.com/thegobi/ithz_mcp/raw/main/ithz_mcp.zip
https://github.com/thegobi/ithz_mcp/raw/main/ithz-mcp-macos.zip
https://github.com/thegobi/ithz_mcp/raw/main/ithz-mcp-ubuntu.tar.gz
https://github.com/thegobi/ithz_mcp/raw/main/ithz-mcp-ubuntu.deb
https://github.com/thegobi/ithz_mcp/raw/main/ithz-native-macos-intel-build-kit.zip
```

Metadata:

```text
server.json
VERSION.json
SHA256SUMS.txt
RELEASE_NOTES.md
```

## Agent Bootstrap

For agent-assisted installation into another project:

1. Copy `ithz_mcp.md` or `install_ithz.md` into the target project.
2. Ask the local coding agent to read that file and install ITHZ MCP.
3. The agent should preserve an existing `project.ithz` if present, configure
   local MCP/Git support, and report exactly what changed.

## Platform Notes

### macOS Intel Native Runtime

`ithz-mcp-macos.zip` installs the Python stdio MCP layer. Native `project.ithz`
storage on Mac Intel additionally needs `ithz-native`, which can be built from
`ithz-native-macos-intel-build-kit.zip`:

```sh
unzip ithz-native-macos-intel-build-kit.zip
cd ithz-native-macos-intel-build-kit
chmod +x native_ithz/macos_native/build_macos_native_package.sh
native_ithz/macos_native/build_macos_native_package.sh --arch x86_64
```

Then install the generated native package:

```sh
cd native_ithz/dist/macos_native/ithz-native-preview-v0.1-alpha-rc2-macos-x86_64
./smoke_test.sh
./install_macos_native.sh
export ITHZ_NATIVE_EXE="$HOME/.local/share/ithz-mcp/native/ithz-native"
```

### Ubuntu/Linux

The Ubuntu package includes `install_ithz.md`, Linux host installers, user-local
wrapper scripts, a Linux native source build kit and extraction-backed fallback
commands:

```sh
tar -xzf ithz-mcp-ubuntu.tar.gz
cd ithz-mcp-ubuntu
./install.sh
./install_linux_native.sh
ithz-mcp version
ithz-native-resolve
```

Native Linux `project.ithz` support uses the bundled build kit and dynamically
loads the system zlib runtime (`libz.so.1` / `libz.so`).

## Status

ITHZ MCP is currently free during alpha preview. Public package metadata is
published on PyPI and in the official MCP Registry.
