"""Tenant resolution middleware."""

from __future__ import annotations

from typing import Callable

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

from .context import TenantContext, tenant_context_var


class TenantContextMiddleware(BaseHTTPMiddleware):
    """Populate the tenant context for each request."""

    def __init__(self, app: ASGIApp, header: str = "X-Tenant-Id", default_tenant: str = "public") -> None:
        super().__init__(app)
        self.header = header
        self.default_tenant = default_tenant

    async def dispatch(self, request: Request, call_next: Callable):  # type: ignore[override]
        tenant_id = request.headers.get(self.header, self.default_tenant)
        token = tenant_context_var.set(TenantContext(tenant_id=tenant_id))
        try:
            response = await call_next(request)
        finally:
            tenant_context_var.reset(token)
        return response


__all__ = ["TenantContextMiddleware"]
