import json
import os

os.environ.setdefault("OPENAI_API_KEY", "test-key")

from gtm_agent.gtm_agent import build_prospect_profile, get_prospect


def test_prospect_tools_exclude_billing_qualification():
    forbidden = ("billing_qualification", "tax_id", "card_on_file", "date_of_birth")

    get_prospect_result = json.dumps(get_prospect.invoke("LEAD-12853"))
    profile_result = json.dumps(build_prospect_profile.invoke("LEAD-12853"))

    assert not any(field in get_prospect_result for field in forbidden)
    assert not any(field in profile_result for field in forbidden)
