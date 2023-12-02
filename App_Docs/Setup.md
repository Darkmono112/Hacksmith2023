## Startup Instructions:

### Requirements 
python version 3.11.* 
Django version 4.1.7+
js

### Database Setup:
The following commands populate the database with example inventory items and drones.  For example, after starting the project for the first time, you should be able to navigate to the Order Page and see various items ready to order. After navigating to the directory that contains 'manage.py' in the DroneCones project, run the following commands in the shell or terminal:

**For Windows:**
```shell
python manage.py make-migrations 
python manage.py migrate 
```

**For Mac:**
```terminal
python3 manage.py make-migrations 
python3 manage.py migrate 
```

### Enabling User Groups:

The following command sets up user groups that separate users into Administrators, Users, and Flyers. One person can be a member of multiple groups.  For instance, someone who just created a new account is a User and can become a flyer by navigating to the Flyer Signup Page and filling out the form.  Without this command, the site would not be able to function properly.  Run the following in the shell or terminal from the same location as the migration commands:

**For Windows:**
```shell
python manage.py create_groups
```

**For Mac:**
```terminal
python3 manage.py create_groups
```

### Startup:
To start the server locally, run the following command from the same location as the previous commands:

**For Windows:**
```shell
python manage.py runserver
```

**For Mac:**
```terminal
python3 manage.py runserver
```

This will serve the application to the web from your computer, meaning that no one else can see the application. If you would like to host the website publicly, stay tuned for the next update!

### Quick Start:
To quick start from the top directory in your project "HACKSMITH2023," run the following in the shell:

**For Windows and Mac:**
```shell
./start.sh
```

This shell script is a convenient way to start or restart the server from any directory in the application.

**Note:**
The Quickstart functionality is not available on Mac at this time. Stay tuned for future updates!
