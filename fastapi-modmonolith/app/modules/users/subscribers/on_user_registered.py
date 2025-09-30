"""Example subscriber for the user registered event."""

from __future__ import annotations

from ....shared.logging import get_logger
from ..domain.events import UserRegistered

logger = get_logger(__name__)


async def on_user_registered(event: UserRegistered) -> None:
    logger.info("user_registered", user_id=str(event.user_id), tenant_id=event.tenant_id)


__all__ = ["on_user_registered"]
