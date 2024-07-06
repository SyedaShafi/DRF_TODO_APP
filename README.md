
# MyTodo
The MyTodo App is a web application that allows users to manage their tasks effectively. Users can sign up, log in, create tasks, set due dates and priorities, and sort tasks based on different criteria.

## Features
1. Token-based Authentication: Secure account activation through email.

2. Task Management: Users can create, read, update, and delete tasks.

3. Task Attributes: Set due dates and priorities for tasks.

4. Sorting: Sort tasks by priority, due date, and status.


## Technologies Used
1. Frontend: HTML, CSS, Bootstrap, JavaScript
2. Backend: Django REST Framework
3. Deployment: Render


### Installation
1. Clone the repository:
````bash
git clone https://github.com/SyedaShafi/DRF_TODO_APP/
cd DRF_TODO_APP
````
2. Create and activate a virtual environment:
````bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
````
3. Install the dependencies:
````bash
pip install -r requirements.txt
````
4. Apply migrations:
````bash
python manage.py migrate
````

5. Create a superuser:
````bash
python manage.py createsuperuser
````
6. Run the development server:
````bash
python manage.py runserver
````
7. Open your browser and navigate to http://127.0.0.1:8000 to see the application.

## Contact
Your Name -syedashafi4@gmail.com

Project Link: https://drf-todo-app.onrender.com/
