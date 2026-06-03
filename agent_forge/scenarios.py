from __future__ import annotations

from pathlib import Path

import yaml

from .models import Scenario


def load_scenario(path: str | Path) -> Scenario:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    return Scenario(
        name=data["name"],
        request=data["request"],
        domain=data.get("domain", "general"),
        amount_usd=int(data.get("amount_usd", 0)),
        risk_hint=data.get("risk_hint", "low"),
        required_tools=list(data.get("required_tools", [])),
        facts=list(data.get("facts", [])),
    )