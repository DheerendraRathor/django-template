# Django Template

This is a simple template to initialize django project with default configuration.
Currently it is designed to work with postgresql.

# Features:
- Pre configured with eslint, pylint and isort
- Separate settings for local development and production
- Separate requirements file for local and production and test environment
- All apps in one directory
- Provided a core application which you can use like util app
- Overridden startapp command to create new application in apps directory

# Installation
- Install cookiecutter (`pip install cookiecutter`)
- Go to directory where you want to install your project
- Run `cookiecutter /path/to/django-template`, this will ask few settings from you, provide them.
- Go to project directory. Read README in project directory.

# All cookiecutter settings
- **project_name**: A human readable project name,
- **description**: A short description for Project,
- **django_project_name**: Name of your Django project directory
- **django_version**: "1.9.5",
- **apps_directory**: Directory where you should keep all apps. Default is apps,
- **core_app_name**: Name of core application. Default core. Suggestions: utils, common,
- **database_host**: Postgresql Db host. Default localhost,
- **database_port**: Postgresql Db port. Default 5432,
- **database_name**: Db name. Default: Name of your project,
- **database_user**: Db username. Default name of your project,
- **database_password**: Db password. Default: name of your project,
- **max_line_length**: Maximum line length settings. Default 79 (PEP8).
