"""
startapp command overrrides Django's default startapp command.

This startapp command creates apps into apps directory specified by DEFAULT_APPS_DIRECTORY
specified in settings.
"""

import fileinput
import os

import shutil
from django.core.management import CommandError
from django.core.management.commands.startapp import Command as StartAppCommand
from django.conf import settings


class Command(StartAppCommand):

    def handle(self, **options):
        directory = options.get('directory', None)
        # directory key is already present in options which is None.
        name = options['name']

        full_path = None
        if not directory:
            """
            If directory is not provided then use DEFAULT_APPS_DIRECTORY.

            This block creates DEFAULT_APPS_DIRECTORY/app_name directory and
            pass that path to default startapp command.
            """
            directory = os.path.join(settings.BASE_DIR, settings.DEFAULT_APPS_DIRECTORY)
            full_path = os.path.join(directory, name)
            if not os.path.exists(full_path):
                os.makedirs(full_path)
            options['directory'] = full_path

        try:
            super().handle(**options)
            if full_path:
                """
                If apps directory is used then change the app name to DEFAULT_APPS_DIRECTORY.app_name
                in AppConfig
                """
                apps_py = os.path.join(full_path, 'apps.py')
                if os.path.isfile(apps_py):
                    for line in fileinput.input(apps_py, inplace=True):
                        line = line.replace("'%s'" % name, "'%s.%s'" % (settings.DEFAULT_APPS_DIRECTORY, name))
                        print(line, end='')
        except CommandError:
            if full_path:
                shutil.rmtree(full_path)
            raise
