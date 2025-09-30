"""Blog commands."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class PublishPost:
    title: str
    slug: str
    body: str
    tenant_id: str


__all__ = ["PublishPost"]
