"""Entrypoint for running the echo service."""
from __future__ import annotations

import uvicorn

from .app import app


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
