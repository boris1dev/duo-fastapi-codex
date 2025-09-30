"""Command definitions for the users module."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class RegisterUser:
    email: str
    tenant_id: str


__all__ = ["RegisterUser"]
