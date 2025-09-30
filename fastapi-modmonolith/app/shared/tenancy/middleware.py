from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.types import ASGIApp

from app.config import settings

from .context import set_tenant


class TenancyMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        tenant = settings.TENANCY_DEFAULT
        # Header priorisieren
        if hdr := request.headers.get(settings.TENANCY_HEADER):
            tenant = hdr
        else:
            # Subdomain (optional): tenant.example.com → tenant
            host = request.headers.get("host", "")
            if "." in host:
                sub = host.split(":")[0].split(".")[0]
                if sub and sub not in ("www", "localhost"):
                    tenant = sub
        set_tenant(tenant)
        response = await call_next(request)
        response.headers["X-Tenant"] = tenant
        return response


__all__ = ["TenancyMiddleware"]
