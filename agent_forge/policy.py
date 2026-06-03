from __future__ import annotations


def approval_required(risk: str, amount_usd: int = 0) -> bool:
    return risk in {"high", "critical"} or amount_usd >= 50000


def policy_decision(tool_risks: list[str], amount_usd: int = 0) -> dict:
    highest = "high" if "high" in tool_risks else "medium" if "medium" in tool_risks else "low"
    required = approval_required(highest, amount_usd)
    return {"highest_risk": highest, "approval_required": required, "approver": "VP Customer Success" if required else None}