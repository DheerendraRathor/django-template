# Installations

- Install required software

```lang=bash
sudo apt-get update
sudo apt-get install python3-pip python3.5-dev libpq-dev postgresql postgresql-contrib memcached \
libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev libxml2-dev libxslt1-dev libffi-dev nodejs \
npm
```

- Create a postgresql user and database. Taken from
[postgresql wiki](https://wiki.postgresql.org/wiki/First_steps).

```lang=bash
sudo su - postgres
psql # Now you must be in postgresql command line mode

CREATE DATABASE {{cookiecutter.database_name}};
CREATE USER {{cookiecutter.database_user}} WITH PASSWORD '{{cookiecutter.database_password}}';
GRANT ALL PRIVILEGES ON DATABASE {{cookiecutter.database_name}} TO {{cookiecutter.database_user}};
\q
exit
```

- Install configured lint tools
```lang=bash
sudo npm install -g csslint jsonlint eslint
```
