"""Blog domain entities."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4

from .events import PostPublished
from .value_objects import Slug


@dataclass(slots=True)
class Post:
    id: UUID
    title: str
    slug: Slug
    body: str
    tenant_id: str
    published_at: datetime | None = None

    @classmethod
    def publish(cls, title: str, body: str, slug: Slug, tenant_id: str) -> tuple["Post", PostPublished]:
        post = cls(id=uuid4(), title=title, slug=slug, body=body, tenant_id=tenant_id, published_at=datetime.utcnow())
        event = PostPublished(name="post_published", post_id=post.id, tenant_id=tenant_id)
        return post, event


__all__ = ["Post"]
