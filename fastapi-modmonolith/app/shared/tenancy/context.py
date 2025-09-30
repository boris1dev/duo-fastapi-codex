from contextvars import ContextVar

from app.config import settings


_tenant: ContextVar[str] = ContextVar("tenant", default=settings.TENANCY_DEFAULT)


def set_tenant(tenant: str):
    _tenant.set(tenant)


def get_tenant() -> str:
    return _tenant.get()


__all__ = ["set_tenant", "get_tenant"]
