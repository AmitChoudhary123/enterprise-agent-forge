from __future__ import annotations


def render_text(outcome: dict) -> str:
    lines = [
        f"Scenario: {outcome['scenario']}",
        f"Domain: {outcome['domain']}",
        f"Risk: {outcome['policy']['highest_risk']}",
        f"Approval required: {outcome['policy']['approval_required']}",
        f"Blocked: {outcome['policy']['blocked']}",
        "",
        "Tool outputs:",
    ]
    for item in outcome["results"]:
        lines.append(f"- {item['name']} [{item['risk']}]: {item['output']}")
    lines.extend(["", "Controls:"])
    for control in outcome["policy"]["controls"] or ["standard monitoring"]:
        lines.append(f"- {control}")
    lines.extend(["", "Audit trail:"])
    for event in outcome["audit_log"]:
        lines.append(f"- {event['kind']}: {event['message']}")
    return "\n".join(lines)


def render_markdown(outcome: dict) -> str:
    lines = [
        f"# Agent Run Report: {outcome['scenario']}",
        "",
        f"**Domain:** {outcome['domain']}",
        f"**Risk:** {outcome['policy']['highest_risk']}",
        f"**Approval required:** {outcome['policy']['approval_required']}",
        f"**Blocked:** {outcome['policy']['blocked']}",
        "",
        "## Tool Outputs",
    ]
    for item in outcome["results"]:
        lines.append(f"- **{item['name']}** ({item['risk']}): {item['output']}")
    lines.extend(["", "## Controls"])
    for control in outcome["policy"]["controls"] or ["standard monitoring"]:
        lines.append(f"- {control}")
    lines.extend(["", "## Audit Trail"])
    for event in outcome["audit_log"]:
        lines.append(f"- `{event['kind']}` {event['message']}")
    return "\n".join(lines)