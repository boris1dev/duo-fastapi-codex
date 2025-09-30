"""Simplified transactional outbox placeholder."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4


@dataclass(slots=True)
class OutboxMessage:
    """Represents a message waiting to be published."""

    id: UUID
    topic: str
    payload: dict
    created_at: datetime

    @classmethod
    def create(cls, topic: str, payload: dict) -> "OutboxMessage":
        return cls(id=uuid4(), topic=topic, payload=payload, created_at=datetime.utcnow())


__all__ = ["OutboxMessage"]
