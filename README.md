# FastAPI REST Web Application

This is a FastAPI-based Article Microservice that allows users to create, read, update, and delete articles. The service is secured with JWT authentication, where tokens are issued by a separate Authentication Microservice.

## Features

- Create a new article
- Get a list of all articles
- Get a specific article by ID
- Update an existing article by ID
- Delete a article by ID
- JWT-based authentication for all endpoints


## Project Structure

```
.
├── .env
├── app
│   ├── __init__.py
│   ├── dto
│   │   ├── __init__.py
│   │   ├── article_dto.py
│   ├── model
│   │   ├── __init__.py
│   │   ├── article.py
│   ├── repository
│   │   ├── __init__.py
│   │   ├── article_repository.py
│   ├── service
│   │   ├── __init__.py
│   │   ├── article_service.py
│   ├── controller
│   │   ├── __init__.py
│   │   ├── article_controller.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── logger_config.py
│   │   ├── database.py
│   │   ├── log_middleware.py
        ├── env_settings.py
│   └── main.py
```

## Getting Started

### Prerequisites

- Python 3.7+
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- Starlette
- A database variable specified in a `.env` file

### Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/yourusername/fastapi-postgresql-oauth2-article-microservice.git
   cd fastapi-postgresql-oauth2-article-microservice.git
   ```

2. **Create and activate a virtual environment**:

   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Create a `.env` file**:

   ```sh
   echo "DATABASE_PORT=5432" > .env
   ```

### Running the Application

To run the application, use the following command:

```sh
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## Project Components

### DTO Classes

Located in the `app/dto/article_dto.py` file, these classes handle the data transfer objects for requests and responses, validated using Pydantic.

### Model Classes

Located in the `app/model/article.py` file, these classes define the database schema using SQLAlchemy.

### Database Configuration

Located in the `app/core/database.py` file, this class handles the database engine and session creation, using settings loaded from a `.env` file.

### Repository Classes

Located in the `app/repository/article_repository.py` file, these classes handle database operations like insert, update, delete, and select.

### Service Classes

Located in the `app/service/article_service.py` file, these classes contain business logic and interact with repository classes to perform operations.

### Controller Classes

Located in the `app/controller/article_controller.py` file, these classes define the FastAPI endpoints for the application.

### Middleware

Custom logging middleware is located in the `app/core/log_middleware.py` file. CORS middleware is added in `app/main.py`.

## API Endpoints

### Authentication

All endpoints require a valid JWT token issued by the Authentication Microservice. Obtain the token by authenticating with the `/auth/login` endpoint of the Authentication Microservice.


## Example Usage

### Create a article

```sh
curl -X 'POST' \
  'http://127.0.0.1:8000/articles/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJI' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "My First article",
  "content": "This is the content of my first article."
}'
```

### Get a article

```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/articles/1' \
  -H 'accept: application/json'
  -H 'Authorization: Bearer eyJhbGciOiJI' \
```

### Update a article

```sh
curl -X 'PUT' \
  'http://127.0.0.1:8000/articles/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJI' \
  -d '{
  "title": "Updated article Title",
  "content": "Updated content of my article."
}'
```

### Delete a article

```sh
curl -X 'DELETE' \
  'http://127.0.0.1:8000/articles/1' \
  -H 'accept: application/json'
  -H 'Authorization: Bearer eyJhbGciOiJI' \
```

### Get All articles

```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/articles/' \
  -H 'accept: application/json'
  -H 'Authorization: Bearer eyJhbGciOiJI' \
```

## License

This project is licensed under the MIT License.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

