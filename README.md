# Tweeter Jr

## (A twitter clone app using django and python)

Here is a simple twitter clone app using django and python bootstrap.  
This project uses sqlite3 and django models for the database and bootstrap for frontend.
To use it and test it follow these instructions:
<br><br>

### 1. Download project

Download the project into your devise or simply clone the project into your virtual environment or any directory
you want by running the
command :

```commandline
git clone https://github.com/HB2102/Twitter-Clone-Django
```

### 2. Install requirements

First you should install the requirements of the project, for that, go to the project directory and run the command :

```commandline
pip install -r requirements/requirements.txt
```

and wait for pip to install packages.

### 3. Run the project

For running the project, go to its directory and run the command :

```commandline
python manage.py runserver
```

if you get the error that the port is in use you can change the port by running the command like :

```commandline
python manage.py runserver 5000
```

and it'll change the port to 5000 but running it on port 8000 should be fine at the beginning.  
When the project is running you can go to the URL that it shows on your browser and see the first page.

### 4. Use Project

You can see accounts and tweets, you can register as a user and send tweets, like them, share them, change your info, password and so many other things.

You also can do everything you want as an admin. database already has one default admin with default values of :

- Username : admin
- Password : admin

you can login as admin and add users and profiles, edit them, remove them, promote other users to admin and...
<br><br><br>
Thanks for your time.