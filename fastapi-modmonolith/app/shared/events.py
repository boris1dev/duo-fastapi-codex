"""Simple in-process domain events."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, runtime_checkable


@dataclass(slots=True)
class Event:
    """Base class for domain events."""

    name: str


@runtime_checkable
class EventHandler(Protocol):
    """Protocol for event handlers."""

    async def __call__(self, event: Event) -> None: ...


__all__ = ["Event", "EventHandler"]
