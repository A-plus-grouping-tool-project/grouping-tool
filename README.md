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
    TOKEN = ''`

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
