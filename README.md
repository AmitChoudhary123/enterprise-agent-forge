# Enterprise Agent Forge

A lightweight enterprise agent runtime for building auditable AI agents with tools, memory, approvals, and business controls.

## Why this exists

The most visible AI agent projects prove that developers want runnable agents, not static portfolio notes. Enterprise teams need the same energy, but with controls: audit logs, approval gates, policy checks, and deterministic demos that can be reviewed without secrets or cloud spend.

## What it does

Enterprise Agent Forge ships a small but useful agent loop:

- Planner that turns a business request into executable steps
- Tool registry for deterministic business tools
- Memory store for reusable context
- Approval policy for risky actions
- Audit log for every plan, tool call, and decision
- CLI demo that runs with no API keys

## Demo

```bash
python demo/run_demo.py
```

Example request:

> Prepare a customer churn action plan and check whether executive approval is needed.

The demo plans the work, calls tools, records memory, applies an approval rule, and prints an audit trail.

## Architecture

```text
User request -> Planner -> Policy gate -> Tool registry -> Memory -> Audit log -> Final response
```

## Repository structure

```text
agent_forge/          Core runtime
configs/              Policy and tool settings
data/                 Sample enterprise records
demo/                 Runnable demo
docs/                 Architecture, examples, contribution guide
tests/                Unit tests
```

## Quick start

```bash
python -m venv .venv
pip install -r requirements.txt
pytest -q
python demo/run_demo.py
```

## Community roadmap

- Add OpenAI / local model adapter interfaces
- Add pluggable vector memory
- Add FastAPI service wrapper
- Add Slack/Jira/GitHub tool examples
- Add policy templates for finance, HR, legal, and operations

## Enterprise relevance

This project demonstrates agentic AI in the style enterprises actually need: useful automation with accountability, policy gates, observability, and reproducible behavior.