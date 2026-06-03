# Model Adapter Roadmap

The base runtime is deterministic so contributors can understand and test the system without API keys.

Planned adapter interface:

```python
class PlannerAdapter:
    def plan(self, scenario, available_tools):
        ...
```

Initial adapters to add:

- OpenAI planner
- Ollama/local planner
- Rules-only planner baseline

The policy engine should remain deterministic even when planning uses an LLM.