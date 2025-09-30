"""In-process message bus for commands and events."""

from __future__ import annotations

from collections import defaultdict
from typing import Any, Awaitable, Callable

from .events import Event, EventHandler


Handler = Callable[[Any], Awaitable[Any]]


class MessageBus:
    """Async message bus supporting command and event dispatch."""

    def __init__(self) -> None:
        self._event_handlers: dict[type[Event], list[EventHandler]] = defaultdict(list)
        self._command_handlers: dict[type[Any], Handler] = {}

    def register_event_handler(self, event_type: type[Event], handler: EventHandler) -> None:
        self._event_handlers[event_type].append(handler)

    def register_command_handler(self, command_type: type[Any], handler: Handler) -> None:
        self._command_handlers[command_type] = handler

    async def handle(self, message: Any) -> Any:
        handler = self._command_handlers.get(type(message))
        if handler:
            return await handler(message)
        if isinstance(message, Event):
            await self._handle_event(message)
            return None
        raise ValueError(f"No handler registered for message type {type(message)!r}")

    async def _handle_event(self, event: Event) -> None:
        for handler in self._event_handlers.get(type(event), []):
            await handler(event)


__all__ = ["MessageBus"]
