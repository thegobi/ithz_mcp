from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from ithz_mcp import BUILD_ID, VERSION
from ithz_mcp.ccg.court import CCG_VERSION, CourtRunner, default_constitution, initialize_project
from ithz_mcp.ccg.mcp_server import handle_request, tool_schemas
from ithz_mcp.ccg.models import ScriptedBackend
from ithz_mcp.ccg.settings_store import DEFAULTS


EXPECTED_TOOLS = {
    "ccg_status",
    "ccg_initialize_project",
    "ccg_run_case",
    "ccg_execute_demo",
    "ccg_get_case",
    "ccg_verify_case",
    "ccg_list_cases",
}


class PublicCCGReleaseTests(unittest.TestCase):
    def test_release_identity_and_generic_baseline(self) -> None:
        self.assertEqual(VERSION, "0.1.0a7")
        self.assertEqual(BUILD_ID, "public-generic-mcp35-cached-prefix-multilab.20260827.1")
        self.assertEqual(CCG_VERSION, "mcp35.0-cached-prefix-current-projection-multilab-v1")
        self.assertEqual(default_constitution()["constitution_id"], "ccg-universal-baseline")

    def test_public_mcp_surface_is_exact(self) -> None:
        names = {schema["name"] for schema in tool_schemas()}
        self.assertEqual(names, EXPECTED_TOOLS)

    def test_scripted_status_and_mcp_handshake(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            initialized = initialize_project(project)
            self.assertTrue(initialized["created"])
            runner = CourtRunner(project, codex_backend=ScriptedBackend())
            status = runner.status()
            self.assertEqual(status["ccg_version"], CCG_VERSION)
            self.assertEqual(status["case_count"], 0)
            response = handle_request(
                {
                    "jsonrpc": "2.0",
                    "id": 1,
                    "method": "initialize",
                    "params": {"protocolVersion": "2024-11-05"},
                },
                project,
            )
            self.assertEqual(response["result"]["serverInfo"]["version"], VERSION)

    def test_low_cost_model_defaults(self) -> None:
        self.assertEqual(DEFAULTS["opponent_2_provider"], "gemini")
        self.assertEqual(DEFAULTS["gemini_model"], "gemini-3.7-flash")
        self.assertEqual(DEFAULTS["gemini_thinking_level"], "low")
        self.assertEqual(DEFAULTS["daybreak_policy"], "high_and_critical")


if __name__ == "__main__":
    unittest.main(verbosity=2)
