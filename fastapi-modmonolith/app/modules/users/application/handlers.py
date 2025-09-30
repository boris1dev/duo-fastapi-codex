"""Command and query handlers for users."""

from __future__ import annotations

from typing import Iterable

from ..domain.services import register_user
from ..infrastructure import InMemoryUserRepository
from .commands import RegisterUser
from .queries import ListUsers

_repository = InMemoryUserRepository()


async def register_user_handler(command: RegisterUser) -> dict:
    result = await register_user(command.email, command.tenant_id)
    if result.is_failure:
        raise ValueError(result.error)
    await _repository.add(result.value)
    return {"id": str(result.value.id), "email": str(result.value.email)}


async def list_users_handler(query: ListUsers) -> Iterable[dict]:
    users = await _repository.list(limit=query.limit)
    return [{"id": str(u.id), "email": str(u.email)} for u in users]


__all__ = ["register_user_handler", "list_users_handler"]
