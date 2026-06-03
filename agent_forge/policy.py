from __future__ import annotations

RISK_ORDER = {"low": 1, "medium": 2, "high": 3, "critical": 4}


def highest_risk(risks: list[str]) -> str:
    if not risks:
        return "low"
    return max(risks, key=lambda item: RISK_ORDER.get(item, 0))


def policy_decision(tool_risks: list[str], amount_usd: int = 0, risk_hint: str = "low") -> dict:
    risk = highest_risk(tool_risks + [risk_hint])
    approval_required = risk in {"high", "critical"} or amount_usd >= 50000
    blocked = risk == "critical" and amount_usd >= 250000
    controls = []
    if approval_required:
        controls.append("named business approval")
    if risk in {"high", "critical"}:
        controls.extend(["rollback plan", "audit retention", "post-action review"])
    if amount_usd >= 50000:
        controls.append("financial controller review")
    return {
        "highest_risk": risk,
        "approval_required": approval_required,
        "blocked": blocked,
        "approver": "VP-level business owner" if approval_required else None,
        "controls": controls,
    }