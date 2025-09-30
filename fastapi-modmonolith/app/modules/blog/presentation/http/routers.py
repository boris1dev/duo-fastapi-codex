"""API routes for blog posts."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ....shared.tenancy.context import tenant_context_var
from ...application.commands import PublishPost
from ...application.handlers import list_posts_handler, publish_post_handler
from ...application.queries import ListPosts

router = APIRouter(tags=["blog"])


class PostCreateRequest(BaseModel):
    title: str
    slug: str
    body: str


class PostResponse(BaseModel):
    id: str
    title: str
    slug: str


@router.post("/", response_model=PostResponse, status_code=201)
async def create_post(payload: PostCreateRequest) -> PostResponse:
    tenant_context = tenant_context_var.get()
    if not tenant_context:
        raise HTTPException(status_code=400, detail="Tenant context missing")
    result = await publish_post_handler(
        PublishPost(title=payload.title, slug=payload.slug, body=payload.body, tenant_id=tenant_context.tenant_id)
    )
    return PostResponse(**result)


@router.get("/", response_model=list[PostResponse])
async def list_posts(limit: int = 20) -> list[PostResponse]:
    items = await list_posts_handler(ListPosts(limit=limit))
    return [PostResponse(**item) for item in items]
