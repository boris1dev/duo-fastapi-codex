"""Blog queries."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ListPosts:
    limit: int = 20


__all__ = ["ListPosts"]
