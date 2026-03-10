# Project1

A Django web application.

## Prerequisites

- Python 3.12+
- Docker & Docker Compose (optional)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/nukarapusai/Project1.git
cd Project1
```

### 2. Set up environment variables

```bash
cp .env.example .env
```

Edit `.env` and set a secure `DJANGO_SECRET_KEY`. You can generate one with:

```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

### 3. Install dependencies

```bash
cd myapp
pip install -r requirements.txt
```

### 4. Run the development server

```bash
python manage.py migrate
python manage.py runserver
```

The app will be available at http://localhost:8000.

## Running with Docker

```bash
cd myapp
docker-compose up --build
```

## Environment Variables

| Variable           | Description                              | Default               |
|--------------------|------------------------------------------|-----------------------|
| `DJANGO_SECRET_KEY`| Django secret key (required in production) | `change-me-in-production` |
| `DEBUG`            | Enable debug mode (`True`/`False`)       | `False`               |
| `ALLOWED_HOSTS`    | Comma-separated list of allowed hosts    | *(empty)*             |

> ⚠️ **Never** commit your `.env` file or expose your `DJANGO_SECRET_KEY` publicly.
