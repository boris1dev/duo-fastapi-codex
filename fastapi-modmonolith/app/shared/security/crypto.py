"""Crypto utilities used by the OIDC verifier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def read_jwks(path: str | Path) -> dict[str, Any]:
    """Read a JWKS file from disk."""

    with Path(path).expanduser().open("r", encoding="utf-8") as fp:
        return json.load(fp)


__all__ = ["read_jwks"]
