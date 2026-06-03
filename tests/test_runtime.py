from pathlib import Path

from agent_forge.policy import policy_decision
from agent_forge.runtime import AgentRuntime
from agent_forge.scenarios import load_scenario


def test_customer_scenario_runs_with_audit_trail():
    scenario = load_scenario(Path("configs/scenarios/customer_retention.yml"))
    outcome = AgentRuntime().run(scenario)
    assert outcome["scenario"] == "Customer retention intervention"
    assert len(outcome["results"]) == 3
    assert any(event["kind"] == "POLICY" for event in outcome["audit_log"])


def test_procurement_scenario_requires_approval():
    scenario = load_scenario(Path("configs/scenarios/procurement_risk.yml"))
    outcome = AgentRuntime().run(scenario)
    assert outcome["policy"]["approval_required"] is True
    assert "financial controller review" in outcome["policy"]["controls"]


def test_policy_blocks_critical_large_actions():
    decision = policy_decision(["critical"], amount_usd=300000)
    assert decision["blocked"] is True