# 🏛 Full-Stack Architecture Overview

**Tech Stack**:

* **Backend**: Python (FastAPI, Flask, or Django)
* **Frontend**: Vue 3 (TypeScript, Composition API, Pinia)

---

## 🔰 Core Principles

### 1. Separation of Concerns (SoC)

Keep responsibilities separated:

* Backend: Route → Service → Repository → Model
* Frontend: Component → Composable → Store → API client → Backend

### 2. Single Responsibility Principle (SRP)

Each unit (function/class/module/component) should do one thing well.

### 3. Layered Architecture

Organize code in clear, horizontal layers:

#### Backend Layers:

```
┌────────────┐
│  Routers   │ → HTTP interface (FastAPI endpoints)
├────────────┤
│ Services   │ → Business logic, use cases
├────────────┤
│ Repositories│ → Database operations
├────────────┤
│ Models     │ → Pydantic schemas & ORM models
└────────────┘
```

#### Frontend Layers:

```
┌────────────┐
│ Components │ → UI pieces (smart or dumb)
├────────────┤
│ Composables│ → Shared logic hooks
├────────────┤
│ Stores     │ → Global state (Pinia)
├────────────┤
│ API Client │ → Abstracted Axios/Fetch
└────────────┘
```

---

## 🧱 Backend Design Principles (Python)

### 4. Typed Schemas with Pydantic

Use models for input validation and output shaping.

### 5. Service Layer Encapsulation

Put business logic in services, not route handlers.

### 6. Repository Abstraction

Use repository classes for all DB operations to enable testability and separation.

### 7. Config & Environment Separation

Use `.env` + `pydantic.BaseSettings` to load configuration per environment.

---

## 🌐 Frontend Principles (Vue 3 + TS)

### 8. Type-Safe Component Design

Use full TypeScript definitions for props, emits, and composables.

### 9. Smart vs Dumb Components

Separate UI-only components from data-aware components.

### 10. Pinia State Stores

Use stores per feature; avoid bloated global state. Leverage composables.

### 11. API Layer Abstraction

Centralize API calls with Axios in a dedicated service layer.

---

## 🔐 Cross-Cutting Concerns

### 12. Input Validation Everywhere

Backend: Pydantic models
Frontend: Zod, Yup or inline validation

### 13. Authn & Authz Separation

* JWT or OAuth2 for authentication
* Middleware/dependencies for authorization rules

### 14. Uniform Error Handling

Standard error response shapes. Custom exception handlers in FastAPI. User feedback on frontend.

---

## 📦 Advanced Patterns

### 15. Modular Monorepo Structure (optional)

```
/monorepo
  /frontend
  /backend
  /common (shared types)
```

### 16. GraphQL (if used)

* Schema first or code-first
* Resolvers delegate to service layer
* Use codegen for shared typings

### 17. Testing Strategy

* Backend: pytest (+ mocks for repos)
* Frontend: Vitest/Jest + Playwright for E2E

---

## ⚙️ DevOps & Infrastructure

### 18. Environment Config

* `.env.dev`, `.env.prod`
* Load via `dotenv` (Python) and `import.meta.env` (Vite)

### 19. CI/CD & Formatting

* Lint: black, ruff (Python), eslint + prettier (TS)
* Automate tests + deploy with GitHub Actions or GitLab CI

### 20. Observability

* Backend: structlog, loguru, Sentry, Prometheus
* Frontend: sentry-vue, console logging, UX-level error capture

---
## 🛰 Microservices Architecture

This repository demonstrates a lightweight microservices setup. The main entry
point is an **API Gateway** implemented with FastAPI. It proxies requests to the
individual services.

### Services

- **Auth Service** – Provides user registration and login backed by PostgreSQL.
- **Echo Service** – Simple test service returning the provided message.

Each service exposes its own OpenAPI schema and runs independently. They can be
deployed separately and scaled as needed.

The gateway simply forwards requests to the appropriate service. Additional
services can be mounted by extending the gateway configuration.

---

## 🧭 Summary

* Start simple, grow modular
* Validate inputs at all layers
* Use typed contracts between frontend and backend
* Keep code testable and business logic cleanly separated
* Document your decisions

> Keep this document updated as the architecture evolves.
