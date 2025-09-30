"""API routes for the users module."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr

from ....shared.tenancy.context import tenant_context_var
from ...application.commands import RegisterUser
from ...application.handlers import list_users_handler, register_user_handler
from ...application.queries import ListUsers

router = APIRouter(tags=["users"])


class UserCreateRequest(BaseModel):
    email: EmailStr


class UserResponse(BaseModel):
    id: str
    email: EmailStr


@router.post("/", response_model=UserResponse, status_code=201)
async def create_user(payload: UserCreateRequest) -> UserResponse:
    tenant_context = tenant_context_var.get()
    if not tenant_context:
        raise HTTPException(status_code=400, detail="Tenant context missing")
    result = await register_user_handler(RegisterUser(email=payload.email, tenant_id=tenant_context.tenant_id))
    return UserResponse(**result)


@router.get("/", response_model=list[UserResponse])
async def list_users(limit: int = 20) -> list[UserResponse]:
    items = await list_users_handler(ListUsers(limit=limit))
    return [UserResponse(**item) for item in items]
