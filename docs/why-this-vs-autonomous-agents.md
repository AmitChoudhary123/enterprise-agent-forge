# Why This Instead of Another Autonomous Agent?

Enterprise Agent Forge is not trying to clone large autonomous agent projects. It focuses on the gap those projects often leave for enterprise teams.

## Different design goal

| Common agent demo | Enterprise Agent Forge |
| --- | --- |
| Maximize autonomy | Maximize controlled autonomy |
| LLM-first behavior | Policy-first runtime with optional LLM adapters |
| Impressive one-off task | Repeatable scenario packs |
| Hard to audit | Audit trail by default |
| Tool use as capability | Tool use plus approval and governance |
| Success by anecdote | Success by scenario tests and reports |

## When to use this project

Use it when you need to explain or prototype:

- Human-in-the-loop agent workflows
- Risk-based approval gates
- Audit-ready enterprise agents
- Agent operating model design
- Safe extension patterns for business tools

## When not to use it

Do not use it as a replacement for full agent platforms, browser automation agents, or multi-model assistants. It is a compact reference implementation for governance-first enterprise agent design.