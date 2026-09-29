import os
import unittest

os.environ.setdefault("OPENAI_API_KEY", "test-key")
from gtm_agent.gtm_agent import send_prospect_email


class SendProspectEmailTests(unittest.TestCase):
    def test_blocks_disqualified_prospect(self):
        result = send_prospect_email.func(
            {"prospect_id": "LEAD-50001", "name": "Disqualified Lead", "email": "lead@example.com"},
            "Follow up",
            "Hello",
            runtime=None,
            from_rep={"name": "Rep", "email": "rep@example.com"},
        )

        self.assertEqual(result["status"], "blocked")

    def test_sends_qualified_prospect(self):
        result = send_prospect_email.func(
            {"prospect_id": "LEAD-12853", "name": "Qualified Lead", "email": "lead@example.com"},
            "Follow up",
            "Hello",
            runtime=None,
            from_rep={"name": "Rep", "email": "rep@example.com"},
        )

        self.assertEqual(result["status"], "sent")


if __name__ == "__main__":
    unittest.main()
