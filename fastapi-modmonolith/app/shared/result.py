from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar("T")


@dataclass
class Result(Generic[T]):
    ok: bool
    value: Optional[T] = None
    error: Optional[str] = None

    @staticmethod
    def success(v: T | None = None):
        return Result(True, v, None)

    @staticmethod
    def failure(msg: str):
        return Result(False, None, msg)
