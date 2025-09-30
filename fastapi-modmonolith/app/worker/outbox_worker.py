"""Simple async worker that would process outbox messages."""

from __future__ import annotations

import asyncio

from ..config import get_settings
from ..logging import get_logger


async def run_outbox_worker() -> None:
    settings = get_settings()
    logger = get_logger(__name__)
    poll_interval = settings.outbox_poll_ms / 1000
    logger.info("outbox_worker_started", poll_interval=poll_interval)
    while True:  # pragma: no cover - illustrative
        await asyncio.sleep(poll_interval)
        logger.debug("outbox_worker_tick")


if __name__ == "__main__":
    asyncio.run(run_outbox_worker())
