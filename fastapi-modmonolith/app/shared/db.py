from sqlalchemy import create_engine, event, text
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import settings
from app.shared.tenancy import get_tenant


class Base(DeclarativeBase):
    pass


def _dsn() -> str:
    return (
        f"postgresql+psycopg://{settings.DB_USER}:{settings.DB_PASSWORD}"
        f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
    )


engine = create_engine(_dsn(), echo=settings.DB_ECHO, pool_pre_ping=True)


class TenantSession(Session):
    pass


SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, class_=TenantSession)


@event.listens_for(TenantSession, "after_begin")
def _apply_tenant(session, transaction, connection):
    tenant = get_tenant() or settings.TENANCY_DEFAULT
    session.info["tenant"] = tenant
    if settings.TENANCY_MODE == "schema":
        connection.execute(text("SET search_path TO :tenant, public"), {"tenant": tenant})
    else:
        connection.execute(text("SELECT set_config('app.current_tenant', :tenant, true)"), {"tenant": tenant})


@event.listens_for(engine, "checkout")
def _reset_tenant(dbapi_connection, connection_record, connection_proxy):
    if settings.TENANCY_MODE == "schema":
        with dbapi_connection.cursor() as cursor:
            cursor.execute("SET search_path TO %s, public", (settings.TENANCY_DEFAULT,))
    else:
        with dbapi_connection.cursor() as cursor:
            cursor.execute(
                "SELECT set_config('app.current_tenant', %s, true)",
                (settings.TENANCY_DEFAULT,),
            )
