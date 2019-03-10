# grouping-tool
A tool for managing groups in A+

#### Setting up the development environment
1. You need to have installed and created a virtual environment to run this program (see https://packaging.python.org/guides/installing-using-pip-and-virtualenv/ for more information about setting up a virtual environment).

2. Activate virtual environment

3. Install project dependencies

    `pip3 install -r requirements.txt`

4. Create a PostgreSQL database. If you don't yet have PostgreSQL installed see installation instructions for [Windows](http://www.postgresqltutorial.com/install-postgresql/),
[Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04) and [Mac OS](https://medium.com/@Umesh_Kafle/postgresql-and-postgis-installation-in-mac-os-87fa98a6814d).

5. Create a file `credentials.py` to `project/project` and add your database credentials in form:
`DB_USERNAME = 'username'
    DB_PASSWORD = 'password'
    DB_NAME = 'dbname'
    API_TOKEN = ''`

   You can get your user token from the user settings of your local A+,
   but an empty token is enough to get the program running.

5. Run migrations
    `python3 manage.py migrate`

#### Running local test server
1. Activate virtualenv

2. From project root, start test server on localhost:7000 (or any port you prefer except 8000)

    `python3 manage.py runserver 7000`

#### Adding data by shell to models
1. Activate virtualenv

2. Open shell
    `python3 manage.py shell`

3. Import your model
    ex. `from app.models import Student`

4. Create model object
    ex. `student = Student(1234,"username", "student id","email")`

5. Save object
    ex. `student.save()`

6. If your model has ManyToManyField create model object like this
    ex. `group = Group(group_id=101,course_code="course_code",group_type=1)`

7. Add object to ManyToManyField (remember to save objects before adding)
    ex. `group.students.add(student)`

#### Running aplus server to test back-end

1. Follow the steps in the README of apluslms/course-templates repository
    https://github.com/apluslms/course-templates
  
2. Populate the database of aplus server instance with students and enroll them to course 1 for example

3. Navigate to app/group_students
    ex. `localhost:7000/app/group_students`
    
4. Check table `groups` in the database used by the grouping-tool tool
    
#### Setting up a working LTI authentication between development aplus and grouper-tool

1. Activate your grouper-tool venv, and navigate to grouper-tool's manage.py location

2. remember to (re)install requirements.txt packages

3. run database migrations

4. Run python manage.py add_lti_key -d "some description"

5. Copy the key and secret somewhere for later use

6. Run grouper-tool server (remember to designate some non-default port)

7. Now run another terminal, activate Aplus venv and start your aplus development server

8. Open the admin interface within your web browser (localhost:aplusport/admin)

9. Choose lti services and click add service

10. Fill some of the fields as described below:

- `Url: http://localhost:"PORT HERE"/auth/lti_login` NOTE: replace "PORT HERE" with your port!

- Destination region: hosted internally

- Menu label: grouper

- Check Enabled

- Access settings: Public service, no API access

- Consumer key: Paste the key you saved earlier

- Consumer secret: Paste the secret you saved earlier

- Hit save

11. Navigate to some test course from your aplus frontpage (logged in as admin)

12. Click edit course > Menu > Add new menu item > choose the recently added lti service from the services list > Send

13. You should now see a new grouper menu item on the left side pane, clicking it will authenticate and redirect you to grouper's teacher view

