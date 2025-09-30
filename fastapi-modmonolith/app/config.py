"""Application configuration using Pydantic settings."""

from functools import lru_cache
from typing import Literal

from pydantic import AnyHttpUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Typed configuration loaded from environment variables."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_env: Literal["dev", "prod", "test"] = Field(default="dev", validation_alias="APP_ENV")
    app_debug: bool = Field(default=True, validation_alias="APP_DEBUG")
    app_host: str = Field(default="0.0.0.0", validation_alias="APP_HOST")
    app_port: int = Field(default=8000, validation_alias="APP_PORT")

    db_host: str = Field(default="localhost", validation_alias="DB_HOST")
    db_port: int = Field(default=5432, validation_alias="DB_PORT")
    db_user: str = Field(default="app", validation_alias="DB_USER")
    db_password: str = Field(default="app", validation_alias="DB_PASSWORD")
    db_name: str = Field(default="app", validation_alias="DB_NAME")
    db_echo: bool = Field(default=False, validation_alias="DB_ECHO")

    redis_host: str = Field(default="localhost", validation_alias="REDIS_HOST")
    redis_port: int = Field(default=6379, validation_alias="REDIS_PORT")

    tenancy_mode: Literal["row", "schema"] = Field(default="row", validation_alias="TENANCY_MODE")
    tenancy_header: str = Field(default="X-Tenant-Id", validation_alias="TENANCY_HEADER")
    tenancy_default: str = Field(default="public", validation_alias="TENANCY_DEFAULT")

    oidc_enabled: bool = Field(default=True, validation_alias="OIDC_ENABLED")
    oidc_issuer: AnyHttpUrl | None = Field(default=None, validation_alias="OIDC_ISSUER")
    oidc_audience: str | None = Field(default=None, validation_alias="OIDC_AUDIENCE")
    oidc_jwks_path: str | None = Field(default=None, validation_alias="OIDC_JWKS_PATH")

    dev_jwt_sub: str | None = Field(default=None, validation_alias="DEV_JWT_SUB")
    dev_jwt_email: str | None = Field(default=None, validation_alias="DEV_JWT_EMAIL")
    dev_tenant: str | None = Field(default=None, validation_alias="DEV_TENANT")

    jwt_alg: str = Field(default="RS256", validation_alias="JWT_ALG")

    outbox_poll_ms: int = Field(default=500, validation_alias="OUTBOX_POLL_MS")


@lru_cache
def get_settings() -> Settings:
    """Return cached settings instance."""

    return Settings()


__all__ = ["Settings", "get_settings"]
