"""Mappers for blog domain entities."""

from __future__ import annotations

from ..domain.entities import Post


def post_to_dict(post: Post) -> dict:
    return {
        "id": str(post.id),
        "title": post.title,
        "slug": str(post.slug),
        "tenant_id": post.tenant_id,
        "published_at": post.published_at.isoformat() if post.published_at else None,
    }


__all__ = ["post_to_dict"]
