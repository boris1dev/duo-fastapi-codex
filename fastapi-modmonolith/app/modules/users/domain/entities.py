"""Domain entities for the users module."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from .events import UserRegistered
from .value_objects import Email


@dataclass(slots=True)
class User:
    """Aggregate root representing a system user."""

    id: UUID
    email: Email
    tenant_id: str
    created_at: datetime = field(default_factory=datetime.utcnow)

    @classmethod
    def register(cls, email: Email, tenant_id: str) -> tuple["User", UserRegistered]:
        user = cls(id=uuid4(), email=email, tenant_id=tenant_id)
        event = UserRegistered(name="user_registered", user_id=user.id, tenant_id=tenant_id)
        return user, event


__all__ = ["User"]
