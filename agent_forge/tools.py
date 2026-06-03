from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class ToolResult:
    name: str
    output: str
    risk: str = "low"


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, Callable[[str], ToolResult]] = {}

    def register(self, name: str, func: Callable[[str], ToolResult]) -> None:
        self._tools[name] = func

    def run(self, name: str, argument: str) -> ToolResult:
        if name not in self._tools:
            raise KeyError(f"Unknown tool: {name}")
        return self._tools[name](argument)


def customer_health_tool(argument: str) -> ToolResult:
    if "churn" in argument.lower():
        return ToolResult("customer_health", "Churn risk is high: usage down 31%, NPS down 18 points.", "medium")
    return ToolResult("customer_health", "Customer health is stable.", "low")


def action_plan_tool(argument: str) -> ToolResult:
    return ToolResult(
        "action_plan",
        "Recommended plan: executive sponsor call, retention offer, product adoption workshop, weekly success review.",
        "medium",
    )