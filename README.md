# Demo API

## Environment

### Prerequisite

- python 3.12.0

### Install python dependencies

- `brew install pyenv pipenv`
- `pipenv install`
  
### Django ORM migrations

> Run these two commands only when changes are made to the Django models

```bash
# create migration files
python manage.py makemigrations
# or
pipenv run makemigrations

# apply the migration operations
python manage.py migrate
# or
pipenv run migrate
```

### Run development server

create `.env`  in root directory, you can see the `.env.sample`

```bash
python manage.py runserver
```

It will start a local server at `localhost:8000` and you can access the API
The API document at `localhost:8000/redoc/`


### Testing

```bash
python manage.py test
```

## API Document

This project uses [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/) to generate the Redoc and OpenAPI schema.

- Redoc
  - [http://localhost:8000/redoc/](http://localhost:8000/redoc/)
- OpenApi 3.0 Schema (JSON)
  - [http://localhost:8000/schema/](http://localhost:8000/schema/)

