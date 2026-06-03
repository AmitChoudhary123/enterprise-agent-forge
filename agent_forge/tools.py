from __future__ import annotations

from typing import Callable

from .models import ToolResult


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, Callable[[str], ToolResult]] = {}

    def register(self, name: str, func: Callable[[str], ToolResult]) -> None:
        self._tools[name] = func

    def names(self) -> list[str]:
        return sorted(self._tools)

    def run(self, name: str, argument: str) -> ToolResult:
        if name not in self._tools:
            raise KeyError(f"Unknown tool: {name}")
        return self._tools[name](argument)


def customer_health(argument: str) -> ToolResult:
    text = argument.lower()
    if "churn" in text or "retention" in text:
        return ToolResult(
            "customer_health",
            "High churn risk: usage down 31%, renewal sentiment negative, executive sponsor inactive.",
            "medium",
            {"signals": ["usage_drop", "negative_sentiment", "inactive_sponsor"]},
        )
    return ToolResult("customer_health", "Customer health is stable.", "low")


def action_plan(argument: str) -> ToolResult:
    return ToolResult(
        "action_plan",
        "Plan: sponsor call, quantified value recap, adoption workshop, retention offer, weekly success review.",
        "medium",
        {"owner": "Customer Success", "cadence": "weekly"},
    )


def procurement_risk(argument: str) -> ToolResult:
    return ToolResult(
        "procurement_risk",
        "Supplier risk elevated: single-region dependency, delayed SOC2 renewal, and price increase above threshold.",
        "high",
        {"risk_drivers": ["concentration", "compliance", "cost"]},
    )


def incident_triage(argument: str) -> ToolResult:
    return ToolResult(
        "incident_triage",
        "Incident severity P1: customer-facing AI answer quality degraded; business owner and model owner must be notified.",
        "high",
        {"severity": "P1", "notify_within_minutes": 30},
    )


def knowledge_lookup(argument: str) -> ToolResult:
    return ToolResult(
        "knowledge_lookup",
        "Relevant policy: high-risk AI actions require named owner, rollback plan, and auditable approval record.",
        "low",
        {"source": "AI-GOV-004"},
    )


def default_registry() -> ToolRegistry:
    registry = ToolRegistry()
    registry.register("customer_health", customer_health)
    registry.register("action_plan", action_plan)
    registry.register("procurement_risk", procurement_risk)
    registry.register("incident_triage", incident_triage)
    registry.register("knowledge_lookup", knowledge_lookup)
    return registry