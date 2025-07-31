# Legendary Memory

## Project Overview

This repository contains a prototype microservices architecture built with Python 3.13 and FastAPI. The project features an API Gateway that proxies requests to individual microservices. Two basic services are included:

- **Auth Service** – Handles user registration and authentication.
- **Echo Service** – Simple utility service used for testing connectivity.

All services expose interactive API documentation using Swagger UI and ReDoc.

## Installation Instructions

1. Ensure Python 3.13 is installed.
2. Install dependencies:

```bash
pip install -e .[redis]
```

3. Run the services individually or via the gateway.

## Usage Guide

Each microservice can be started independently using its `main.py` module. For example:

```bash
python -m services.auth.main  # Auth service on port 8001
python -m services.echo.main  # Echo service on port 8002
python -m gateway.main        # API Gateway on port 8000
```

Visit `http://localhost:8000/docs` to view the gateway API documentation.

## Examples

Register a user through the gateway:

```bash
curl -X POST "http://localhost:8000/auth/register" -H "Content-Type: application/json" -d '{"username": "alice", "password": "secret"}'
```

## Contributing Guidelines

1. Fork the repository and create your feature branch.
2. Write unit tests for new functionality.
3. Run `ruff` for linting and `pytest` for testing before opening a pull request.
4. Submit a pull request with a clear description of your changes.

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.
