"""Unit of work abstractions."""

from __future__ import annotations

from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from .db import SessionFactory


class AbstractUnitOfWork(ABC):
    """Base class for implementing a unit of work."""

    session: AsyncSession

    async def __aenter__(self) -> "AbstractUnitOfWork":
        self.session = await self._get_session()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:  # type: ignore[override]
        if exc:
            await self.rollback()
        else:
            await self.commit()
        await self.session.close()

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()

    @abstractmethod
    async def _get_session(self) -> AsyncSession:
        ...


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    """Default SQLAlchemy implementation."""

    async def _get_session(self) -> AsyncSession:
        return SessionFactory()


__all__ = ["AbstractUnitOfWork", "SqlAlchemyUnitOfWork"]
