"""Value objects for blog posts."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Slug:
    value: str

    def __post_init__(self) -> None:
        if not self.value or " " in self.value:
            raise ValueError("Slug must be a non-empty string without spaces")

    def __str__(self) -> str:
        return self.value


__all__ = ["Slug"]
