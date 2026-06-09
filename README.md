# ITHZ-MCP package

This repository carries the installable ITHZ-MCP package artifacts, not the
full development source tree.

Use it like this:

1. Copy `ithz_mcp.md` into the target project.
2. Ask the local coding agent: `See ithz_mcp.md and install`.
3. The agent clones this package repository, expands `ithz_mcp.zip` or
   `ithz-mcp-macos.zip`, runs smoke checks, initializes the current project,
   reuses an existing `project.ithz` if present, and configures local
   MCP/Git-driver support.
4. If the user gives durable workflow, decision, gate or risk instructions, the write-enabled MCP profile stores them as typed memory in `project.ithz`.

Repository:

```text
https://github.com/thegobi/ithz_mcp.git
```

Direct package URL:

```text
https://github.com/thegobi/ithz_mcp/raw/main/ithz_mcp.zip
```

macOS MCP package URL:

```text
https://github.com/thegobi/ithz_mcp/raw/main/ithz-mcp-macos.zip
```

Ubuntu/Linux package URLs:

```text
https://github.com/thegobi/ithz_mcp/raw/main/ithz-mcp-ubuntu.tar.gz
https://github.com/thegobi/ithz_mcp/raw/main/ithz-mcp-ubuntu.deb
```

macOS Intel native build kit URL:

```text
https://github.com/thegobi/ithz_mcp/raw/main/ithz-native-macos-intel-build-kit.zip
```

## macOS Intel native runtime

`ithz-mcp-macos.zip` installs the Python stdio MCP layer. Native
`project.ithz` storage on Mac Intel additionally needs `ithz-native`, which can
be built from `ithz-native-macos-intel-build-kit.zip`:

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

## Ubuntu/Linux

The Ubuntu package includes `install_ithz.md`, Linux host installers, fixed
user-local wrapper scripts, a Linux native source build kit and extraction-backed
fallback commands:

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

Package metadata:

```text
VERSION.json
SHA256SUMS.txt
```

The artifact name is stable. Build identity, source commit and package hash live in `VERSION.json` and `SHA256SUMS.txt`; old package versions belong in Git history or releases, not as many ZIP files in `main`.

ITHZ-MCP does not replace Git, a production database, cloud sync, host chat history, vector databases, or every retrieval system.
