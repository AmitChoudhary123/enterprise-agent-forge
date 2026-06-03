from agent_forge import AgentRuntime
from agent_forge.policy import approval_required


def test_agent_runs_tools_and_records_audit_log():
    outcome = AgentRuntime().run("Prepare a customer churn action plan")
    assert len(outcome["results"]) == 2
    assert any("TOOL customer_health" in line for line in outcome["audit_log"])


def test_policy_requires_approval_for_large_amount():
    assert approval_required("low", amount_usd=75000) is True