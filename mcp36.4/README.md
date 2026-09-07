# ITHZ MCP36.4 Pregame Integration

Python package version: `0.1.0a13`.
Upstream build: `product-candidate-mcp36.4-opt-in-canary.20260902.1`.
Local compatibility patch: `preserve-read-evidence-v1`.

This directory publishes the compatibility patch, regression tests and constitution used for the verified Pregame Simulator MCP upgrade. It does not replace or relabel the older platform binaries in the repository root. No PyPI or registry release is implied. The full internal source distribution contains unrelated organization-specific profiles and is deliberately not published here.

## Apply to an Existing MCP36.4 Source Checkout

Requires Python 3.10 or later and an existing MCP36.4 source checkout. Review and apply the patch from that checkout's root:

```sh
git apply --check /path/to/preserve-read-evidence.patch
git apply /path/to/preserve-read-evidence.patch
```

For native project.ithz storage, configure a compatible native executable explicitly with ITHZ_NATIVE_EXE. This integration pack does not contain an installable Python distribution or a new platform-native build. Back up existing archives and verify compatibility before ingestion. Project-local MCP profiles should pin their interpreter and explicit project path. Canary execution remains off unless separately authorized.

## Compatibility Fix

Read responses were being compacted into write-receipt fields, discarding search hits and status/integrity evidence. The patch preserves sanitized read results, while retaining compact successful write receipts. Existing tool names, arguments and JSON-RPC envelopes remain unchanged.

The private archive used during integration testing is deliberately not published. Its read-only and write-enabled MCP profiles passed initialize, tools/list, archive status, constitution retrieval and memory integrity checks; read checks preserved the archive hash. Those local integration results do not certify every platform or CCG capability.

## Project Constitution

See [Pregame Constitution](examples/pregame/CONSTITUTION.md). It documents honest tier comparisons, no-lookahead validation, provenance, scoring consistency and release boundaries. It is policy, not a technical permission gateway. It does not authorize production actions.

## Tests

```sh
python -m unittest discover -s /path/to/mcp36.4/tests -v
```

Run against your MCP36.4 environment. All 19 tests passed locally on 2026-09-07. Tests cover memory integrity, canary controls and response preservation. No provider calls or live sports-feed requests are needed. SOURCE_SHA256.json records published artifact hashes.
