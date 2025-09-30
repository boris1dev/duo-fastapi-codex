"""Domain services for users."""

from __future__ import annotations

from ....shared.result import Result
from .entities import User
from .value_objects import Email


async def register_user(email: str, tenant_id: str) -> Result[User, str]:
    """Simple domain service to register a user."""

    try:
        email_vo = Email(email)
    except ValueError as exc:
        return Result(error=str(exc))

    user, event = User.register(email_vo, tenant_id)
    return Result(value=user)


__all__ = ["register_user"]
