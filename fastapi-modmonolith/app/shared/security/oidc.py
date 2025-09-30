"""OIDC token verification helpers."""

from __future__ import annotations

from pathlib import Path

from authlib.jose import JsonWebToken
from authlib.jose.errors import JoseError
from jose import jwt

from ..config import get_settings
from .crypto import read_jwks


class OIDCVerifier:
    """Very small wrapper around Authlib and python-jose for development use."""

    def __init__(self, jwks_path: str | None = None) -> None:
        settings = get_settings()
        self.issuer = settings.oidc_issuer
        self.audience = settings.oidc_audience
        self.jwt_alg = settings.jwt_alg
        path_value = jwks_path or settings.oidc_jwks_path
        self.jwks_path = Path(path_value) if path_value else None
        self._jwt = JsonWebToken([self.jwt_alg])

    def load_keys(self) -> dict:
        if not self.jwks_path:
            raise RuntimeError("JWKS path is not configured")
        return read_jwks(self.jwks_path)

    def verify(self, token: str) -> dict:
        try:
            jwks = self.load_keys()
            return self._jwt.decode(
                token,
                jwks,
                claims_options={"iss": {"values": [self.issuer]}, "aud": {"values": [self.audience]}},
            )
        except JoseError:
            # fallback to python-jose for local debugging
            return jwt.decode(
                token,
                self.load_keys(),
                algorithms=[self.jwt_alg],
                audience=self.audience,
                issuer=self.issuer,
            )


__all__ = ["OIDCVerifier"]
