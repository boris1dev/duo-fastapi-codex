"""Handlers for blog commands and queries."""

from __future__ import annotations

from typing import Iterable

from ..domain.entities import Post
from ..domain.value_objects import Slug
from ..infrastructure import InMemoryPostRepository
from .commands import PublishPost
from .queries import ListPosts

_repository = InMemoryPostRepository()


async def publish_post_handler(command: PublishPost) -> dict:
    slug = Slug(command.slug)
    post, _event = Post.publish(title=command.title, body=command.body, slug=slug, tenant_id=command.tenant_id)
    await _repository.add(post)
    return {"id": str(post.id), "title": post.title, "slug": str(post.slug)}


async def list_posts_handler(query: ListPosts) -> Iterable[dict]:
    posts = await _repository.list(limit=query.limit)
    return [
        {
            "id": str(post.id),
            "title": post.title,
            "slug": str(post.slug),
        }
        for post in posts
    ]


__all__ = ["publish_post_handler", "list_posts_handler"]
