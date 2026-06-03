from pathlib import Path

from agent_forge.reports import render_text
from agent_forge.runtime import AgentRuntime
from agent_forge.scenarios import load_scenario

if __name__ == "__main__":
    scenario = load_scenario(Path("configs/scenarios/customer_retention.yml"))
    outcome = AgentRuntime().run(scenario)
    print(render_text(outcome))