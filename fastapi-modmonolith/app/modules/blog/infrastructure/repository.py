"""Post repository abstraction."""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Dict

from ..domain.entities import Post


class PostRepository(ABC):
    @abstractmethod
    async def add(self, post: Post) -> None: ...

    @abstractmethod
    async def list(self, limit: int = 20) -> Iterable[Post]: ...


class InMemoryPostRepository(PostRepository):
    def __init__(self) -> None:
        self._posts: Dict[str, Post] = {}

    async def add(self, post: Post) -> None:
        self._posts[str(post.id)] = post

    async def list(self, limit: int = 20) -> Iterable[Post]:
        return list(self._posts.values())[:limit]


__all__ = ["PostRepository", "InMemoryPostRepository"]
