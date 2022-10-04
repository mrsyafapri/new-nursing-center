# New Nursing Center

## How to use this  project?

- Clone or download this repository to your local machine
- Create a virtual environment `virtualenv venv`
- Activate the virtual environment `source venv/bin/activate`(Linux) or `source venv/Scripts/activate`(Windows)
- Install dependencies using `pip install -r requirements.txt`

### Migrate Database

Run `python manage.py makemigrations` and `python manage.py migrate` to migrate the database.

### Create Admin User

Run `python manage.py createsuperuser` to create an admin user.

### Start Project

Run `python manage.py runserver` to start the project.

### Admin Panel

- Go to `http://localhost:8000/admin` to access the admin panel.
- Login with the credentials you created in the previous step.

## Please give star to this project if you like it or fork it if you want to improve it.
