"""Mapping utilities between domain objects and persistence models."""

from __future__ import annotations

from ..domain.entities import User


def user_to_dict(user: User) -> dict:
    return {
        "id": str(user.id),
        "email": str(user.email),
        "tenant_id": user.tenant_id,
        "created_at": user.created_at.isoformat(),
    }


__all__ = ["user_to_dict"]
