# DATABASE MIGRATION STEPS
## 1. POSTGRESQL
- Be sure that "alembic" and "pg8000" libraries are installed on the project environment!
- If not, run the following commands on the command prompt in the given order:
```sh
pip install alembic
pip install pg8000
alembic init migrations
```
- Change the relevant section in the newly generated "alembic.ini" file:
```
sqlalchemy.url = postgresql+pg8000://admin:Sbulduk2023!@192.168.174.128:5432/TSMDB
```
- Add the given lines to the very most top part of the "env.py" file which is located under "migrations" folder. This part specifies where the "BASE" class is located and in which files related with. In this example, the initialization file is located under Models/__init__.py file.
```sh
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```
## 2. MSSQL