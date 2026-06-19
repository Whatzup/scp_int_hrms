# SCP HVAC Employee Tool

A Django + PostgreSQL MVP for managing HVAC employees, service jobs, job assignments, and field-work status for Super Cool Projects.

## Stack

- Django
- PostgreSQL
- Django templates
- HTML and CSS
- Docker Compose for local PostgreSQL

## Features

- HVAC employee profiles with technician type, skills, certifications, service area, availability, and status
- Employee database fields for employee code, Aadhaar number, name, DOB, gender, contact/address, hire date, reporting manager, salary/rate, profile photo, certificate, and vehicle details
- Clickable employee names with reporting hierarchy such as Technician -> Supervisor -> Manager -> CEO
- Service job records with customer, site address, equipment type, job type, supervisor, dates, and status
- Job task assignment by service job and technician
- Priority, due date, and status tracking
- Dashboard metrics for active HVAC employees, active service jobs, pending job tasks, and overdue job tasks
- Django admin for back-office management

## Local Setup

Create and activate a virtual environment:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```sh
pip install -r requirements.txt
```

Create your local environment file:

```sh
cp .env.example .env
```

Start PostgreSQL:

```sh
docker compose up -d
```

PostgreSQL is exposed on local port `5433` to avoid conflicts with other local databases.

Create and apply migrations:

```sh
python manage.py makemigrations
python manage.py migrate
```

Seed sample HVAC data:

```sh
python manage.py seed_office
```

Create an admin user:

```sh
python manage.py createsuperuser
```

Start the app:

```sh
python manage.py runserver
```

Open `http://localhost:8000`.

## Useful Commands

```sh
python manage.py check
python manage.py test
python manage.py shell
```
