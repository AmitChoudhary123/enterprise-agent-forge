from __future__ import annotations

from dataclasses import dataclass, field

from .memory import MemoryStore
from .models import AuditEvent, Scenario
from .policy import policy_decision
from .tools import ToolRegistry, default_registry


@dataclass
class AgentRuntime:
    tools: ToolRegistry = field(default_factory=default_registry)
    memory: MemoryStore = field(default_factory=MemoryStore)
    audit_log: list[AuditEvent] = field(default_factory=list)

    def audit(self, kind: str, message: str, **detail) -> None:
        self.audit_log.append(AuditEvent(kind=kind, message=message, detail=detail))

    def plan(self, scenario: Scenario) -> list[str]:
        if scenario.required_tools:
            steps = scenario.required_tools
        elif scenario.domain == "customer_success":
            steps = ["customer_health", "action_plan", "knowledge_lookup"]
        elif scenario.domain == "procurement":
            steps = ["procurement_risk", "knowledge_lookup", "action_plan"]
        elif scenario.domain == "incident_management":
            steps = ["incident_triage", "knowledge_lookup", "action_plan"]
        else:
            steps = ["knowledge_lookup", "action_plan"]
        self.audit("PLAN", f"Selected tools: {', '.join(steps)}", tools=steps)
        return steps

    def run(self, scenario: Scenario) -> dict:
        self.memory.seed(scenario.facts)
        self.audit("REQUEST", scenario.request, scenario=scenario.name, domain=scenario.domain)
        results = []
        for step in self.plan(scenario):
            result = self.tools.run(step, scenario.request)
            results.append(result)
            self.memory.remember(result.output)
            self.audit("TOOL", f"{result.name} completed", risk=result.risk, output=result.output)
        decision = policy_decision([result.risk for result in results], scenario.amount_usd, scenario.risk_hint)
        self.audit("POLICY", "Policy decision completed", **decision)
        return {
            "scenario": scenario.name,
            "domain": scenario.domain,
            "request": scenario.request,
            "results": [result.__dict__ for result in results],
            "policy": decision,
            "memory": self.memory.facts,
            "audit_log": [event.__dict__ for event in self.audit_log],
        }