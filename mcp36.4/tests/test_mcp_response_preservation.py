import unittest

from ithz_mcp.mcp_server import _mcp_tool_result


class ResponsePreservationTests(unittest.TestCase):
    def test_read_evidence_survives(self):
        cases = [
            {'results': [{'path': 'CONSTITUTION.md', 'text': 'historical evidence'}]},
            {'safe_verify_ok': True, 'schema': 'status'},
            {'schema': 'memory_integrity', 'failures': ['missing evidence']},
            {'text': 'context', 'context_pack_hash': 'test'},
        ]
        for payload in cases:
            with self.subTest(payload=payload):
                result = _mcp_tool_result(payload)
                self.assertEqual(result['structuredContent'], payload)
                self.assertFalse(result['isError'])

    def test_write_receipt_remains_compact(self):
        result = _mcp_tool_result({'appended': True, 'event_count': 2, 'large_payload': 'omit'})
        self.assertEqual(result['structuredContent']['event_count'], 2)
        self.assertNotIn('large_payload', result['structuredContent'])

    def test_failed_write_keeps_failure_evidence(self):
        payload = {'appended': False, 'reason': 'precondition_failed', 'details': {'expected_hash': 'a'}}
        self.assertEqual(_mcp_tool_result(payload)['structuredContent'], payload)


if __name__ == '__main__':
    unittest.main()
