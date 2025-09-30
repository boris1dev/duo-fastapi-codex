"""Blog domain events."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from ....shared.events import Event


@dataclass(slots=True)
class PostPublished(Event):
    post_id: UUID
    tenant_id: str


__all__ = ["PostPublished"]
