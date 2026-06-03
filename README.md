# Enterprise Agent Forge

Enterprise-safe agent runtime with scenario packs, tool governance, approval gates, audit trails, and runnable executive-grade demos.

## Business problem

Most agentic AI proofs of concept show autonomy, but enterprises need controlled autonomy. Business workflows require policy checks, named accountability, rollback paths, audit evidence, and clear approval rules before agents can influence customers, vendors, employees, or regulated decisions.

## Why it matters

Agentic AI will move from copilots to operational workflows. Without governance-by-design, organizations create hidden operational risk: agents take action without approval, tools execute without traceability, and leaders cannot explain what happened after an incident. A credible enterprise agent architecture must make control, evidence, and observability part of the runtime.

## Method / solution overview

Enterprise Agent Forge provides a compact reference implementation for safe agent execution:

- YAML scenario packs model repeatable business workflows
- A deterministic planner selects tools by domain and scenario
- A tool registry isolates business capabilities from orchestration
- A policy engine applies risk, approval, financial, and blocked-action controls
- A memory store captures reusable context
- Audit events and Markdown/text reports make runs reviewable
- Tests and CI validate runtime behavior and demo execution

## Results / expected impact

This project helps AI leaders and engineering teams:

- Explain enterprise-safe agent design without relying on slideware
- Prototype agent operating controls before introducing LLM variability
- Compare use cases by risk and approval complexity
- Give recruiters, architects, and stakeholders a runnable example of agentic AI governance

## Repository structure

```text
agent_forge/              Runtime, CLI, tools, memory, policy, reports
configs/scenarios/        Customer, procurement, and AI incident scenarios
demo/                     One-command demo wrapper
docs/                     Architecture, business case, roadmap, executive POV
tests/                    Runtime and policy tests
.github/workflows/        CI workflow
```

## Setup

```bash
python -m venv .venv
pip install -r requirements.txt
pytest -q
python demo/run_demo.py
```

Run a specific scenario:

```bash
python -m agent_forge.cli run --scenario configs/scenarios/procurement_risk.yml --format markdown
```

## Roadmap

- Add OpenAI and Ollama planner adapters while keeping policy deterministic
- Add JSON trace export for observability platforms
- Add FastAPI service mode
- Add domain tool packs for finance, legal, HR, and customer operations
- Publish GitHub Pages documentation with example reports