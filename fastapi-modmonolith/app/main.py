"""FastAPI application factory."""

from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from .config import Settings, get_settings
from .logging import configure_logging, get_logger
from .shared.messagebus import MessageBus
from .shared.tenancy.middleware import TenancyMiddleware


@asynccontextmanager
def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Application startup/shutdown hooks."""

    logger = get_logger(__name__)
    settings = get_settings()
    configure_logging(debug=settings.app_debug)
    logger.info("application_startup", env=settings.app_env)
    messagebus = MessageBus()
    app.state.messagebus = messagebus
    yield
    logger.info("application_shutdown")


def create_app(settings: Settings | None = None) -> FastAPI:
    """Create and configure the FastAPI application."""

    settings = settings or get_settings()
    app = FastAPI(
        title="FastAPI Modular Monolith",
        version="0.1.0",
        default_response_class=ORJSONResponse,
        lifespan=lifespan,
    )

    app.add_middleware(TenancyMiddleware)

    @app.get("/health", tags=["system"])
    async def health_check() -> dict[str, str]:
        return {"status": "ok"}

    from .modules.users.presentation.http.routers import router as users_router
    from .modules.blog.presentation.http.routers import router as blog_router

    app.include_router(users_router, prefix="/users")
    app.include_router(blog_router, prefix="/blog")

    return app


app = create_app()


__all__ = ["create_app", "app"]
