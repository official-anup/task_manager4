1)Create a Virtual Environment:
python -m venv my_env

2)Activate the Virtual Environment:
my_env\Scripts\activate.bat

3)Install Dependencies
Ensure your virtual environment is activated and then install the necessary packages:

pip install -r requirements.txt


4)Set Up the Database
Run the following commands to set up the database and create the initial migrations:

python manage.py makemigrations
python manage.py migrate


5)Create a Superuser
Create a superuser to access the Django admin panel:

python manage.py createsuperuser


6) Run the Development Server
Start the development server with:

python manage.py runserver




Usage
Web Application
----------------------
Register: Navigate to /register/ to create a new user.

Task List: View the list of tasks at the root URL (/).

Task Detail: View details of a specific task at /tasks/<task_id>/.

Create Task: Create a new task at /tasks/new/.

Edit Task: Edit an existing task at /tasks/<task_id>/edit/.

Delete Task: Delete a task at /tasks/<task_id>/delete/.

Logout: Log out at /accounts/logout/.

API Endpoints
-----------------
List Tasks: GET /api/tasks/

Retrieve Task: GET /api/tasks/<task_id>/

List Users: GET /api/users/

Retrieve User: GET /api/users/<user_id>/
