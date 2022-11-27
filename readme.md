# [TechOverflow](https://github.com/musaib-js/techblog) Server (Project: TechOverflow)

## Local setup instructions
+ Setup virtual environment
```shell
pip install virtualenv
virtualenv venv --python=python3.6
```
Now activate the environment shell with:
```shell
source venv/bin/activate  # On Linux
```
or
```bat
venv\Scripts\activate  & :: On Windows
```
+ Install all dependencies
```shell
pip install -r requirements.txt
```
+ Database migrations
```
python manage.py makemigrations
python manage.py migrate
```

+ Run Tests
```
python manage.py test
```

+ Finally! Run server
```
python manage.py runserver
```

Open [localhost:8000](http://localhost:8000)

+ To access Django Admin
```
python manage.py createsuperuser
```

When prompted, type your username (lowercase, no spaces), email address, and password.
For example, the output should look like this:

```
Username: nomadadmin
Email address: nomadadmin@techblog.com
Password:
Password (again):
Superuser created successfully.
```

+ Re-run the server
```
python manage.py runserver
```

Open [localhost:8000/admin](http://localhost:8000/admin)
