# Architecture

Enterprise Agent Forge is designed around controlled autonomy. It separates scenario definition, planning, tool execution, policy decisions, memory, and reporting so each concern can be reviewed independently.

## Runtime flow

```text
Scenario YAML -> Scenario loader -> AgentRuntime -> Planner -> ToolRegistry -> PolicyEngine -> MemoryStore -> AuditTrail -> Report
```

## Core components

- `Scenario`: business request, domain, risk hint, amount, required tools, and context facts
- `AgentRuntime`: orchestrates plan, tool execution, memory, audit, and policy
- `ToolRegistry`: isolates callable business capabilities
- `PolicyEngine`: converts risk and value into controls, approvals, and block decisions
- `MemoryStore`: stores scenario facts and generated insights
- `Reports`: converts execution outcomes into text or Markdown artifacts
- `CLI`: enables repeatable scenario execution from a terminal or CI

## Enterprise design decisions

- The base runtime is deterministic so governance can be tested before LLM behavior is introduced
- Policy is independent from planning so model adapters cannot bypass controls
- Tools return risk metadata, not just text
- Audit events are first-class outputs
- Scenario packs are plain YAML so business users and architects can review them

## Extension model

The project is intentionally small. Enterprise teams can add:

- New domain tools
- New scenario packs
- Model planner adapters
- External memory or vector search
- JSON trace export
- API service wrappers