# Architecture

Enterprise Agent Forge is intentionally small. It gives contributors a clear runtime they can extend without reading thousands of lines first.

## Components

- `AgentRuntime`: orchestration loop
- `ToolRegistry`: deterministic tool execution
- `MemoryStore`: simple reusable context
- `policy_decision`: approval gate for risky actions
- `audit_log`: inspectable record of planning, tool calls, and controls

## Design principles

- No API key required for the base demo
- Every action is auditable
- Risk and approval are first-class concepts
- Tools are easy to add and test