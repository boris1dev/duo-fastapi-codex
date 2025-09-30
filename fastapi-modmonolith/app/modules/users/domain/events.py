"""Domain events for users."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from ....shared.events import Event


@dataclass(slots=True)
class UserRegistered(Event):
    """Raised when a new user registers."""

    user_id: UUID
    tenant_id: str


__all__ = ["UserRegistered"]
