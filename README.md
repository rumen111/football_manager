# Football Manager (Django)

Manage teams, players, tactics, and matches. Public landing page, private dashboard, and a customized Django admin.

## Features
- User register/login/logout
- Teams (unique names, logo upload), Players, Tactics (by Profile), Matches (ownership checks)
- Dashboard with “my teams / matches / tactics”
- Admin with list display, filters, search, ordering

## Tech
- Python, Django
- PostgreSQL (dev-ready) or SQLite fallback
- HTML + CSS (no Bootstrap)

## Quick start (SQLite – easiest)
```bash
# Clone
git clone https://github.com/rumen111/football_manager.git
cd football_manager

# Create & activate venv (Windows)
py -m venv .venv
. .venv\Scripts\activate

# Install deps
pip install -r requirements.txt

# Migrate & create admin
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# Run
python manage.py runserver