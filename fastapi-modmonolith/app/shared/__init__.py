"""Shared building blocks for the modular monolith."""

from .db import SessionFactory, engine, get_session
from .events import Event, EventHandler
from .messagebus import MessageBus
from .result import Result
from .uow import AbstractUnitOfWork

__all__ = [
    "SessionFactory",
    "engine",
    "get_session",
    "Event",
    "EventHandler",
    "MessageBus",
    "Result",
    "AbstractUnitOfWork",
]
