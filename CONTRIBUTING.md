# Contributing

Enterprise Agent Forge welcomes practical contributions that make agentic AI safer, clearer, or easier to evaluate.

## Good contributions

- New scenario packs under `configs/scenarios/`
- Deterministic business tools with tests
- Policy controls for approval, rollback, incident response, or audit retention
- Report formats that help executives and architects review an agent run
- Documentation that explains tradeoffs without hype

## Contribution standard

Every meaningful change should include:

- A clear business or engineering reason
- Tests when behavior changes
- A runnable demo update when user-facing behavior changes
- No required secrets for the default path

## Local validation

```bash
pip install -r requirements.txt
pytest -q
python demo/run_demo.py
```