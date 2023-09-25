# LittleLemon
Backstone project for the Meta Backend Developer course.


## Skills used.
- Python (Django).
- HTML, CSS, and Javascript.
- APIs Development.
- Backend Development.
- Database Management (MySQL).

## Running the Project

### Setting up the Environment
Run the following commands to configure the pythons environment.

    pipenv shell
    pipenv install django mysqlclient djangorestframework djoser

### Setting up the Database

Make sure the database is created within MySQL. First login into mysql console.

    mysql -u root -p 

Then create the database.

    CREATE DATABASE LittleLemon;

Then just make sure that you put your password in settings.py.

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'LittleLemon',
            'HOST' : '127.0.0.1',
            'PORT' : '3306',
            'USER' : 'root',
            'PASSWORD' : 'your_password',
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
            }
        }
    }

### Creating Superuser

    pipenv shell
    python manage.py createsuperuser

### Running the server

    pipenv shell
    python manage.py runserver

## Test API End Points

To add an item to the Menu or view the Menu, use the endpoint: 
"http://127.0.0.1:8000/restaurant/menu/"

To add a booking or view the Bookings, use the endpoint:
http://127.0.0.1:8000/restaurant/booking/

To get an auth token, send a POST request to the url:
http://127.0.0.1:8000/auth/token/login/
with the username and password.
