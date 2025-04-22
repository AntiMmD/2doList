# Django To-Do List Application

A web-based task management application built with Django that allows users to create, manage, and track their tasks.

## Features

- User Authentication
  - Custom user model with email and username
  - User registration and login
  - Password hashing for security
  - Protected routes for authenticated users

- Task Management
  - Create new tasks
  - Update existing tasks
  - Delete tasks
  - Search tasks by name
  - View all tasks on homepage


## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/AntiMmD/To2list.git
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Usage

1. Register a new account using email and username
2. Log in with your credentials
3. Create new tasks from the homepage
4. View all your tasks on the homepage
5. Update or delete tasks as needed
6. Use the search functionality to find specific tasks

## Routes

- `/user/signup/` - User registration
- `/user/login/` - User login
- `/user/logout/` - User logout
- `/user/home/` - Homepage with task list
- `/user/add_task/` - Create new task
- `/user/delete_task/<id>/` - Delete specific task
- `/user/update_task/<id>/` - Update specific task
- `/user/search_task/` - Search tasks

## Security Features

- Custom user authentication
- Password hashing
- Login required for task management
- User-specific task access
