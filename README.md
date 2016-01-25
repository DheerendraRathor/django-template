# DJANGO Template Project for Phabricator

## Installation
- Rename all occurence of 'safe' with your project name
- Change 'SAFES' in .arcconfig file to your repository call sign on Phabricator
- Edit `your_project/settings/conf.sample.py` to `your_project/settings/conf.py`

## Setting up local machine for development
- Use Python 3.5
- Install and configure virtualenvwrapper https://virtualenvwrapper.readthedocs.org/en/latest/
- In local machine use `pip install -r requirements/local.txt`
- Edit `your_project/settings/conf.py` to your local settings

## Setting up Production server
- Use Python 3.5
- Install and configure virtualenvwrapper https://virtualenvwrapper.readthedocs.org/en/latest/
- In local machine use `pip install -r requirements/production.txt`
- Edit `your_project/settings/conf.py` to add your production level settings
- Set environment variable `DJANGO_SETTINGS_MODULE` to `your_project.settings.production`
- Continue with Django deployment normally
