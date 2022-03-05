# drf filter

Examples of how to use [django-filter](https://django-filter.readthedocs.io/en/stable) with
[django rest framework](https://www.django-rest-framework.org/).

## Getting Started

### Installation

1. Have Postgres running via docker or your machine
    1. docker
        ```shell
        docker-compose up -d
        ```
2. Setup python development with poetry. Read more at https://python-poetry.org/
    1. Once poetry is installed. Install dependency packages
         ```shell
         poetry install
         ```
3. Create database tables
    ```shell
   python manage.py migrate
    ```
4. Start the server
    ```shell
   python manage.py runserver
    ```
5. Load initial data
   ```shell
   python manage.py load_initial_data
   ```

## View data via django admin

1. Open browser and go to http://localhost:8000/admin/
2. Login as testuser
    |          |          |
    |----------|----------|
    | username | testuser |
    | password | 1234     |

## Swagger
http://localhost:8000/schema/swagger-ui/
