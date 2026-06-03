from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class MemoryStore:
    facts: list[str] = field(default_factory=list)

    def seed(self, facts: list[str]) -> None:
        for fact in facts:
            self.remember(fact)

    def remember(self, fact: str) -> None:
        if fact not in self.facts:
            self.facts.append(fact)

    def recall(self, keyword: str) -> list[str]:
        key = keyword.lower()
        return [fact for fact in self.facts if key in fact.lower()]