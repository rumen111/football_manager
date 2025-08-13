# **Football Manager (Django)**  

A web application to manage **teams**, **players**, **tactics**, and **matches**.  
Features a **public landing page**, **private dashboard**, and a **customized Django admin**.  

---

## **Features**  

- **User Authentication**  
  - Register / Login / Logout  
  - Profile automatically linked to Django User  
- **Teams**  
  - Unique names enforced  
  - Logo upload  
  - Linked to the team’s coach (User)  
- **Players**  
  - Assigned to teams  
  - Positions, nationality, and age tracking  
- **Tactics**  
  - Created by specific profiles  
  - Ownership checks for editing/deletion  
- **Matches**  
  - Home/Away team  
  - Date & score tracking  
- **Dashboard**  
  - "My Teams" / "My Tactics" / "My Matches" views  
- **Admin Panel**  
  - List display, filters, search, ordering  

---

## **Tech Stack**  

- **Backend:** Python, Django  
- **Database:** PostgreSQL (default in this project) or SQLite (for quick testing)  
- **Frontend:** HTML + CSS (custom styling, no Bootstrap)  

---

## **Quick Start**  

```bash
# ==============================
# 1️⃣ PostgreSQL (Default Setup)
# ==============================

# Create the database in PostgreSQL
CREATE DATABASE new_one;

# Ensure PostgreSQL is running on port 5433
#    User: postgres  
#    Password: 0000  

# settings.py should contain:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "new_one",
        "USER": "postgres",
        "PASSWORD": "0000",
        "HOST": "127.0.0.1",
        "PORT": "5433",
    }
}

# ==============================
# 2️⃣ SQLite (Alternative Testing)
# ==============================

# In settings.py, replace DATABASES with:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ==============================
# 3️⃣ Common Steps (PostgreSQL or SQLite)
# ==============================

# Clone repository
git clone https://github.com/rumen111/football_manager.git
cd football_manager

# Create & activate virtual environment (Windows)
py -m venv .venv
. .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run development server
python manage.py runserver

## Live demo
https://rumen111.pythonanywhere.com
