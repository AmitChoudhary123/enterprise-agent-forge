# Usage Guide

Run the default demo:

```bash
python demo/run_demo.py
```

Run a named scenario:

```bash
python -m agent_forge.cli run --scenario configs/scenarios/procurement_risk.yml
```

Render Markdown for sharing:

```bash
python -m agent_forge.cli run --scenario configs/scenarios/ai_incident.yml --format markdown
```

## Add a scenario

Create a YAML file under `configs/scenarios/` with:

```yaml
name: My workflow
domain: customer_success
request: Describe the business request.
amount_usd: 10000
risk_hint: medium
required_tools:
  - knowledge_lookup
  - action_plan
facts:
  - Important context goes here.
```