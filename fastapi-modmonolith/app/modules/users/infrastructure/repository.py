"""User repository abstractions."""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Dict

from ..domain.entities import User


class UserRepository(ABC):
    """Abstract repository interface."""

    @abstractmethod
    async def add(self, user: User) -> None: ...

    @abstractmethod
    async def list(self, limit: int = 20) -> Iterable[User]: ...


class InMemoryUserRepository(UserRepository):
    """Simple repository used during bootstrapping."""

    def __init__(self) -> None:
        self._users: Dict[str, User] = {}

    async def add(self, user: User) -> None:
        self._users[str(user.id)] = user

    async def list(self, limit: int = 20) -> Iterable[User]:
        return list(self._users.values())[:limit]


__all__ = ["UserRepository", "InMemoryUserRepository"]
