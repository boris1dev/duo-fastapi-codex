"""Value objects for the users domain."""

from __future__ import annotations

from dataclasses import dataclass
from pydantic import EmailStr, ValidationError


@dataclass(frozen=True, slots=True)
class Email:
    """Email value object with validation."""

    value: str

    def __post_init__(self) -> None:
        try:
            EmailStr(self.value)
        except ValidationError as exc:  # pragma: no cover - simple example
            raise ValueError("Invalid email address") from exc

    def __str__(self) -> str:
        return self.value


__all__ = ["Email"]
