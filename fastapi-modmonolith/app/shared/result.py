"""Utility result type for application service responses."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")
E = TypeVar("E")


@dataclass(slots=True)
class Result(Generic[T, E]):
    """Represents success or failure."""

    value: T | None = None
    error: E | None = None

    @property
    def is_success(self) -> bool:
        return self.error is None

    @property
    def is_failure(self) -> bool:
        return not self.is_success


__all__ = ["Result"]
