# django_docker_postgres

## Installation

1) Clone this repository.

2) Add file .env.dev:
```

DEBUG=True
SECRET_KEY=&t2f4b2=rylx$m#ocgqxs3942z2vlt79%^ouekc5rbn-ei=)p^
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=notes_django_dev
SQL_USER=notes_django
SQL_PASSWORD=notes_django
SQL_HOST=db
SQL_PORT=5432
```

3) In terminal:

```
$ cd app
$ docker build . # create an image
$ cd ..
$ docker-compose -f docker-compose.yml up -d --build # build image
$ docker-compose -f docker-compose.yml exec web python manage.py migrate # run migrations in "web" container
```

4) Go: 127.0.0.1:8000
