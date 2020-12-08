# Django Custom User with DRF and Simple JWT

According to [Django Document](https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project), it's highly recommended to set up a custom user model when starting a new project. This project is a sample to demo how to create custom user model, and using [Django REST framework](https://www.django-rest-framework.org/) and [SimpleJWT](https://github.com/SimpleJWT/django-rest-framework-simplejwt) for API interface and token based authentication.

Check more detail in my blog post [Django Custom User with DRF and Simple JWT](https://blueswen.github.io/2020/12/06/django-custom-user-with-drf-and-simple-jwt/).

## Dependencies

python >= 3.6

1. Django==3.1.4
2. djangorestframework==3.12.2
3. djangorestframework-simplejwt==4.6.0

## Usage

1. Create python virtualenv

    ```bash
    $ python -m venv .venv
    $ source .venv/bin/activate
    ```

2. Install requirements

    ```bash
    (.venv) $ pip install -r requirements.txt
    ```

3. Migrate DB

    ```bash
    (.venv) $ python manage.py makemigrations
    (.venv) $ python manage.py migrate
    ```

4. Create superuser

    ```bash
    (.venv) $ python manage.py createsuperuser
    ```

5. Run Server

    ```bash
    (.venv) $ python manage.py runserver
    ```

6. Get token from API

    ```bash
    $ curl \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"username": "admin", "password": "admin"}' \
    http://localhost:8000/api/token/

    {"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwNzQ0MzQ3NiwianRpIjoiYzQzYjM2Zjg2ODA0NDU1MzliYzUwNTlmN2YzN2NkMTEiLCJ1c2VyX2lkIjoxfQ.ZC0fAj7HR99v_po4BI-uVVeS9c7ZoN4B35_pYzosE_o","access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA3MzU3Mzc2LCJqdGkiOiIyYjY5NzkxMmZhNjE0NzY3YmJkNDA2NjExMzE1YzkxMCIsInVzZXJfaWQiOjF9.92m-V9vjRxUWGLlcJRFBdLqSHp0UII3SLPTt_yPynqY"}
    ```

7. Get user list with token

    ```bash
    $ curl -H 'Accept: application/json; indent=4' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA3MzU3Mzc2LCJqdGkiOiIyYjY5NzkxMmZhNjE0NzY3YmJkNDA2NjExMzE1YzkxMCIsInVzZXJfaWQiOjF9.92m-V9vjRxUWGLlcJRFBdLqSHp0UII3SLPTt_yPynqY" http://127.0.0.1:8000/api/account/user/
    [
        {
            "id": 1,
            "password": "pbkdf2_sha256$216000$fHERFJ7toIcI$3QOXbA4or+srGXn+60aW+z4rslvJkQcW2wS0oWWzYHI=",
            "last_login": "2020-12-07T16:02:06.847562Z",
            "is_superuser": true,
            "username": "admin",
            "first_name": "",
            "last_name": "",
            "email": "admin@sample.com",
            "is_staff": true,
            "is_active": true,
            "date_joined": "2020-12-07T13:54:21.479125Z",
            "birthday": null,
            "groups": [],
            "user_permissions": []
        }
    ]
    ```

## Reference

1. [Django Custom User Model](https://learndjango.com/tutorials/django-custom-user-model)
2. [Django REST framework](https://www.django-rest-framework.org/)
3. [SimpleJWT Document](https://django-rest-framework-simplejwt.readthedocs.io/)
