from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class MemoryStore:
    facts: list[str] = field(default_factory=list)

    def remember(self, fact: str) -> None:
        self.facts.append(fact)

    def recall(self, keyword: str) -> list[str]:
        key = keyword.lower()
        return [fact for fact in self.facts if key in fact.lower()]