from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass(frozen=True)
class Scenario:
    name: str
    request: str
    domain: str
    amount_usd: int = 0
    risk_hint: str = "low"
    required_tools: list[str] = field(default_factory=list)
    facts: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class ToolResult:
    name: str
    output: str
    risk: str = "low"
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class AuditEvent:
    kind: str
    message: str
    detail: dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())