# Enterprise Agent Forge

Enterprise Agent Forge is a small but useful open-source runtime for building auditable AI agents with tools, memory, policy gates, scenario packs, and reviewable execution reports.

It is intentionally deterministic by default: you can clone it, run it, understand the control flow, and then plug in real model providers later.

## Why people should care

Most agent demos optimize for autonomy. Enterprise teams need something different: autonomy with evidence, approvals, policy checks, incident controls, and an audit trail that leaders can trust.

Enterprise Agent Forge gives teams a practical starting point for those conversations.

## What you can run today

```bash
pip install -r requirements.txt
pytest -q
python -m agent_forge.cli run --scenario configs/scenarios/customer_retention.yml
python -m agent_forge.cli run --scenario configs/scenarios/procurement_risk.yml --format markdown
```

The CLI loads a scenario, plans tool calls, executes deterministic business tools, applies policy controls, writes memory, and prints an audit-ready report.

## Features

- YAML scenario packs for reusable business workflows
- Tool registry with customer, procurement, incident, and knowledge tools
- Policy engine for approval gates and blocked actions
- In-memory context store with recall
- Audit trail and Markdown report generation
- Tests and CI for all core behavior
- Extension docs for adding tools, policies, and model adapters

## Example output

```text
Scenario: Customer retention intervention
Risk: medium
Approval required: False
Tools: customer_health, action_plan, knowledge_lookup
Outcome: Ready for customer-success action with monitored follow-up.
```

## Architecture

```text
Scenario YAML -> AgentRuntime -> Planner -> ToolRegistry -> PolicyEngine -> MemoryStore -> AuditTrail -> Report
```

## Repository map

```text
agent_forge/            Runtime, CLI, policy, tools, reports
configs/scenarios/      Runnable enterprise workflow scenarios
demo/                   One-command demo wrapper
docs/                   Architecture, extension, model adapter, governance docs
tests/                  Unit and scenario tests
```

## Roadmap

- Optional OpenAI/Ollama model planner adapters
- JSON trace export for observability tools
- FastAPI service wrapper
- More domain scenario packs: legal, finance, HR, healthcare, telecom
- GitHub Pages documentation site

## Who this is for

- AI engineers building enterprise-safe agents
- Architects designing agentic operating models
- Data/AI leaders who need governance-by-design examples
- Consultants explaining how agentic AI moves from demo to production