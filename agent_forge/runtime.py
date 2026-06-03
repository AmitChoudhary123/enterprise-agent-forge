from __future__ import annotations

from dataclasses import dataclass, field

from .memory import MemoryStore
from .policy import policy_decision
from .tools import ToolRegistry, ToolResult, action_plan_tool, customer_health_tool


@dataclass
class AgentRuntime:
    tools: ToolRegistry = field(default_factory=ToolRegistry)
    memory: MemoryStore = field(default_factory=MemoryStore)
    audit_log: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.tools.register("customer_health", customer_health_tool)
        self.tools.register("action_plan", action_plan_tool)

    def plan(self, request: str) -> list[str]:
        steps = ["customer_health", "action_plan"] if "customer" in request.lower() or "churn" in request.lower() else ["action_plan"]
        self.audit_log.append(f"PLAN {steps}")
        return steps

    def run(self, request: str, amount_usd: int = 0) -> dict:
        self.audit_log.append(f"REQUEST {request}")
        results: list[ToolResult] = []
        for step in self.plan(request):
            result = self.tools.run(step, request)
            results.append(result)
            self.memory.remember(result.output)
            self.audit_log.append(f"TOOL {result.name} risk={result.risk} output={result.output}")
        decision = policy_decision([result.risk for result in results], amount_usd)
        self.audit_log.append(f"POLICY {decision}")
        return {
            "request": request,
            "results": [result.output for result in results],
            "policy": decision,
            "memory": self.memory.facts,
            "audit_log": self.audit_log,
        }