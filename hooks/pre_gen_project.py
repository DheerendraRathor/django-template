import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.django_project_name }}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: %s is not a valid Django project name!' % module_name)

    # exits with status 1 to indicate failure
    sys.exit(1)

apps_directory = '{{ cookiecutter.apps_directory }}'
if not re.match(MODULE_REGEX, apps_directory):
    print('Error: %s is not a valid name for apps directory!' % apps_directory)
    sys.exit(1)
