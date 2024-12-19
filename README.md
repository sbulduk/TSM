# 1. FOLDER/FILE STRUCTURE OF THE PROJECT

TSM
  - API
    - __init__.py
    - Routes
      - __init__.py
      - AuthRoutes.py
      - Routes.py
    - Services
      - ScriptService
        - Scripts
          - ComputerHelper.ps1
          - GenericHelper.ps1
          - GroupHelper.ps1
          - OUHelper.ps1
          - README.md (already documented)
          - RemoteHelper.ps1
          - UserHelper.ps1
        - __init__.py
        - ScriptService.py
      - __init__.py
      - AuthService.py
      - LogService.py
      - UserService.py
  - Middleware
    - Config
      - DBSettings.toml
      - GenericSettings.toml
    - __init__.py
    - Blueprint.py
    - Config.py
  - migrations
    - env.py
    - ... (remaining migration files)
  - Models
    - __init__.py
    - IModel.py
    - README.md (already documented)
    - Role.py
    - User.py
    - UserRole.py
  - OpenAPI
    - Main.yaml
    - Auth.yaml
  - Venv
  - .env
  - .gitignore
  - alembic.ini
  - App.py
  - requirements.txt

# 2. BACKEND PART
## 2.1 Chosen Libraries for Backend Development
|Library|Explanation|Official Documentation|Pypi Page|
|---|---|---|---|
|Flask|A simple framework for building complex web applications.|[https://flask.palletsprojects.com/en/stable/](https://flask.palletsprojects.com/en/stable/)|[https://pypi.org/project/Flask/](https://pypi.org/project/Flask/)|
|SQLAlchemy|Database Abstraction Library.|[https://docs.sqlalchemy.org/en/20/](https://docs.sqlalchemy.org/en/20/)|[https://pypi.org/project/SQLAlchemy/](https://pypi.org/project/SQLAlchemy/)|
|Alembic|A database migration tool for SQLAlchemy.|[https://alembic.sqlalchemy.org/en/latest/](https://alembic.sqlalchemy.org/en/latest/)|[https://pypi.org/project/alembic/](https://pypi.org/project/alembic/)|
|Connexion|Connexion - API first applications with OpenAPI/Swagger.|[https://connexion.readthedocs.io/en/stable/](https://connexion.readthedocs.io/en/stable/)|[https://pypi.org/project/connexion/](https://pypi.org/project/connexion/)|
|Dependency-Injector|Dependency injection framework for Python.|[https://python-dependency-injector.ets-labs.org/](https://python-dependency-injector.ets-labs.org/)|[https://pypi.org/project/dependency-injector/](https://pypi.org/project/dependency-injector/)|
|Authlib|The ultimate Python library in building OAuth and OpenID Connect servers and clients.|[https://authlib.org/](https://authlib.org/)|[https://pypi.org/project/Authlib/](https://pypi.org/project/Authlib/)|
|Structlog|Structured Logging for Python.|[https://www.structlog.org/en/stable/](https://www.structlog.org/en/stable/)|[https://pypi.org/project/structlog/](https://pypi.org/project/structlog/)|
|Dynaconf|The dynamic configurator for your Python Project.|[https://www.dynaconf.com/](https://www.dynaconf.com/)|[https://pypi.org/project/dynaconf/](https://pypi.org/project/dynaconf/)|
|Redis|Python client for Redis database and key-value store.|[https://redis.readthedocs.io/en/stable/](https://redis.readthedocs.io/en/stable/)|[https://pypi.org/project/redis/](https://pypi.org/project/redis/)|
|Marshmallow|A lightweight library for converting complex datatypes to and from native Python datatypes.|[https://marshmallow.readthedocs.io/en/stable/](https://marshmallow.readthedocs.io/en/stable/)|[https://pypi.org/project/marshmallow/](https://pypi.org/project/marshmallow/)|
|Pytest|pytest: simple powerful testing with Python.|[https://docs.pytest.org/en/stable/](https://docs.pytest.org/en/stable/)|[https://pypi.org/project/pytest/](https://pypi.org/project/pytest/)|