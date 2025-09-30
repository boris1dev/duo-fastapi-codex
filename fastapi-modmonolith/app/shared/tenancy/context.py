"""Context var to hold current tenant information."""

from __future__ import annotations

from contextvars import ContextVar
from dataclasses import dataclass


@dataclass(slots=True)
class TenantContext:
    """Represents the active tenant in the request scope."""

    tenant_id: str


tenant_context_var: ContextVar[TenantContext | None] = ContextVar("tenant_context", default=None)


__all__ = ["TenantContext", "tenant_context_var"]
