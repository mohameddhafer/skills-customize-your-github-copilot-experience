# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small RESTful API using FastAPI and Pydantic. Students will define routes, validate request and response data, and use FastAPI's automatic documentation.

## 📝 Tasks

### 🛠️	Core Implementation

#### Description
Implement a minimal API to manage `Item` resources. Include endpoints to list all items, get an item by id, and create new items.

#### Requirements
Completed program should:

- Provide a FastAPI application with these endpoints: `GET /`, `GET /items`, `GET /items/{id}`, `POST /items`.
- Use Pydantic models for request validation and response schemas.
- Return appropriate HTTP status codes (e.g., 201 for created, 404 for not found).
- Include basic inline documentation and rely on FastAPI's docs at `/docs`.


### 🛠️	Optional Enhancements

#### Description
Add features that demonstrate production practices.

#### Requirements
Completed program should include one or more of the following (optional):

- Add `PUT`/`PATCH` and `DELETE` endpoints.
- Persist data to SQLite using SQLAlchemy or `databases`.
- Add basic authentication (API key) for write endpoints.
- Implement pagination and filtering for `GET /items`.
- Add unit tests for the main endpoints.
