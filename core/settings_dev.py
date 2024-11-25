from .settings_base import *
import os
import dj_database_url

SECRET_KEY = "not really a secret"
DEBUG = True

MIDDLEWARE += [
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

INSTALLED_APPS += [
    "django_browser_reload",
    "whitenoise.runserver_nostatic",
]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# These settings work for the default dev database.
# You can run this database using docker compose.
# Look inside dev_db/README.md for details!!

DB_USER = "pguser"
DB_HOST = "127.0.0.1"
DB_PASSWORD = "password"
DB_NAME = "db"
DB_PORT = 6543

DATABASES = {
    "default": dj_database_url.config(
        default=f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
}
