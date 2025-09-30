"""Query definitions for users."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ListUsers:
    limit: int = 20


__all__ = ["ListUsers"]
