# Example Scenarios

## Customer retention

```bash
python -m agent_forge.cli run --scenario configs/scenarios/customer_retention.yml
```

Shows a customer-success agent that checks churn signals, creates a retention plan, and cites governance guidance.

## Procurement risk

```bash
python -m agent_forge.cli run --scenario configs/scenarios/procurement_risk.yml --format markdown
```

Shows a higher-risk vendor renewal workflow that triggers approval controls and financial review.

## AI incident response

```bash
python -m agent_forge.cli run --scenario configs/scenarios/ai_incident.yml
```

Shows how an AI quality incident can be triaged with severity, notification, rollback, and post-action review controls.