import unittest

from gtm_agent.data_service import (
    fetch_tech_stack,
    get_profile_from_db,
    update_prospect_info,
)


class UpdateProspectInfoTest(unittest.TestCase):
    def test_update_persists_technology_and_invalidates_profile(self):
        update_prospect_info("LEAD-39002", "Terraform")

        self.assertIn("Terraform", fetch_tech_stack("LEAD-39002"))
        profile = get_profile_from_db("LEAD-39002")["prospect_profile"]
        self.assertTrue(profile is None or "Terraform" in profile["tech_stack"])


if __name__ == "__main__":
    unittest.main()
