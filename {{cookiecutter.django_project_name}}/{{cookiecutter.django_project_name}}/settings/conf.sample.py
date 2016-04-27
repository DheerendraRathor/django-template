"""
Configuration file for settings
"""

SECRET_KEY = '<SECRET KEY>'

ALLOWED_HOSTS = ['*']

DB_NAME = '{{cookiecutter.database_name}}'

DB_USERNAME = '{{cookiecutter.database_user}}'

DB_PASSWORD = '{{cookiecutter.database_password}}'

DB_HOST_NAME = '{{cookiecutter.database_host}}'

DB_PORT = '{{cookiecutter.database_port}}'

ADMINS_EMAIL_LIST = [
    # ('Name', 'email@example.com'),
]
