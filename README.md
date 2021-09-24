# Restaurnat API

## Summary
1. [Task](#task)
2. [Launch](#launch)
3. [API documentation](#api_documentation)

## <a name='task'>Task</a>

### C. Build an API server

Build a REST API using Python. Usually, Django REST Framework is a good framework for this
but Flask or Aiohttp, among others, would be appropriate too. It’s a restaurant API where you
can create, update and delete a restaurant (identified by its name), and also list restaurants, get
a restaurant by name and get a random restaurant. Of course, packaging the app and testing it
is always a great plus.

## <a name='launch'>Launch</a>
You need to install Python 3 on your local machine and meet the following conditions:
1. Clone the repository to your local machine
2. In the project root directory, install and run the virtual environment
    - `python3 -m venv venv`
    - `source venv/bin/activate`
4. Install requirements:
    - `pip install -r requirements.txt`
5. Apply all Django migrations:
    - `python3 manage.py makemigrations`
    - `python3 manage.py migrate`
6. In case you need access to the admin panel, create a superuser:
    - `python3 manage.py createsuperuser`
7. Launch local server:
    - `python3 manage.py runserver`

> The app will be available at http://127.0.0.1:8000/

## <a name='api_documentation'>API documentation</a>
You can view the API documentation using various formats. Choose the option that is most convenient for you.

API documentation endpoints:
1. Swagger - `/swagger/`
2. JSON - `/swagger.json`
3. YAML - `/swagger.yaml`

User and JWT creation endpoints:
1. User creation: POST - `/auth​/users​/`
2. JWT creation: POST - `​/auth​/jwt​/create​/`

> JWT must be given in the following format:  
> Authorization: JWT `access_token`
