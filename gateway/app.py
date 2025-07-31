"""API Gateway application that proxies requests to microservices."""
from __future__ import annotations

import os

import httpx
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(title="API Gateway", version="0.1.0")

AUTH_SERVICE_URL = os.environ.get("AUTH_SERVICE_URL", "http://localhost:8001")
ECHO_SERVICE_URL = os.environ.get("ECHO_SERVICE_URL", "http://localhost:8002")

CLIENT_TIMEOUT = httpx.Timeout(10.0)


async def proxy_request(request: Request, base_url: str) -> JSONResponse:
    """Forward an incoming request to the target microservice."""
    async with httpx.AsyncClient(timeout=CLIENT_TIMEOUT) as client:
        url = f"{base_url}{request.url.path}"
        response = await client.request(
            request.method,
            url,
            headers=request.headers.raw,
            params=request.query_params,
            content=await request.body(),
        )
    return JSONResponse(status_code=response.status_code, content=response.json())


@app.api_route("/auth/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def auth_proxy(path: str, request: Request):
    """Proxy requests to the auth service."""
    return await proxy_request(request, AUTH_SERVICE_URL)


@app.api_route("/echo/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def echo_proxy(path: str, request: Request):
    """Proxy requests to the echo service."""
    return await proxy_request(request, ECHO_SERVICE_URL)
