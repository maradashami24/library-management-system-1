# library-management-system-1

# 📚 Library Management System

This is a Django-based Library Management System built using the **Django REST Framework**. It provides a web interface and secure API endpoints for managing books, user registration, authentication (with token-based login), and role-based views for students and admins.

---

## ⚙️ Features

- ✨ Token-based authentication using `rest_framework.authtoken`
- 🔐 Sign up / Sign in endpoints for user login and registration
- 📘 Admin portal to manage (CRUD) books
- 🧑‍🎓 Student portal to view books only
- 🧑‍💻 RESTful APIs for all book-related operations
- 🖥️ Built using Django & DRF

---

### Prerequisites
VS Code (or any text editor)
Python 3+
MySQL Workbench (or MySQL server installed locally)

## 🛠️ Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/maradashami24/library-management-system-1.git
### Make Sure you are in Librarysys folder

2. **Create Virtual Environment (Recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate


3. **Install Dependencies**  
    ```bash
    pip install -r requirements.txt


4. **Database Configuration - Ensure MySQL is installed and running. Then, configure the database settings in settings.py Update the DATABASES section with your MySQL credentials**
    ```bash
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',  # Using MySQL as the backend
            'NAME': 'bookmap_db',                 # Your DB name
            'USER': 'root',                       # DB username
            'PASSWORD': 'jyothi1977',             # DB password
            'HOST': '127.0.0.1',                  # DB host (localhost)
            'PORT': '3306',                       # Default MySQL port
        }
    }

## please add your mysql details in the above section of settings.py file of librarysys project.

5. **Apply Migrations**  
    ```bash
    python manage.py makemigrations
    python manage.py migrate


6. **Create SuperUser (For Admin Access) - (OPTIONAL)**
    ```bash
    python manage.py createsuperuser

7. **Run Development Server**
    ```bash
    python manage.py runserver





