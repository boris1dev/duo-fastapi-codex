from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_ENV: str = "dev"
    APP_DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000

    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "app"
    DB_PASSWORD: str = "app"
    DB_NAME: str = "app"
    DB_ECHO: bool = False

    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    TENANCY_MODE: str = "row"  # row|schema|db
    TENANCY_HEADER: str = "X-Tenant-Id"
    TENANCY_DEFAULT: str = "public"

    OIDC_ENABLED: bool = True
    OIDC_ISSUER: str = "https://dev-issuer.example"
    OIDC_AUDIENCE: str = "app-api"
    OIDC_JWKS_PATH: str | None = None

    DEV_JWT_SUB: str | None = None
    DEV_JWT_EMAIL: str | None = None
    DEV_TENANT: str | None = None

    JWT_ALG: str = "RS256"

    OUTBOX_POLL_MS: int = 500

    model_config = {"env_file": ".env", "extra": "allow"}


settings = Settings()
