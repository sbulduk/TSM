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
|alembic|A database migration tool for SQLAlchemy.|[https://alembic.sqlalchemy.org/en/latest/](https://alembic.sqlalchemy.org/en/latest/)|[https://pypi.org/project/alembic/](https://pypi.org/project/alembic/)|
|connexion|Connexion - API first applications with OpenAPI/Swagger.|[https://connexion.readthedocs.io/en/stable/](https://connexion.readthedocs.io/en/stable/)|[https://pypi.org/project/connexion/](https://pypi.org/project/connexion/)|
|dependency-injector|Dependency injection framework for Python.|[https://python-dependency-injector.ets-labs.org/](https://python-dependency-injector.ets-labs.org/)|[https://pypi.org/project/dependency-injector/](https://pypi.org/project/dependency-injector/)|
|Authlib|The ultimate Python library in building OAuth and OpenID Connect servers and clients.|[https://authlib.org/](https://authlib.org/)|[https://pypi.org/project/Authlib/](https://pypi.org/project/Authlib/)|
|structlog|Structured Logging for Python.|[https://www.structlog.org/en/stable/](https://www.structlog.org/en/stable/)|[https://pypi.org/project/structlog/](https://pypi.org/project/structlog/)|
|dynaconf|The dynamic configurator for your Python Project.|[https://www.dynaconf.com/](https://www.dynaconf.com/)|[https://pypi.org/project/dynaconf/](https://pypi.org/project/dynaconf/)|
|redis|Python client for Redis database and key-value store.|[https://redis.readthedocs.io/en/stable/](https://redis.readthedocs.io/en/stable/)|[https://pypi.org/project/redis/](https://pypi.org/project/redis/)|
|marshmallow|A lightweight library for converting complex datatypes to and from native Python datatypes.|[https://marshmallow.readthedocs.io/en/stable/](https://marshmallow.readthedocs.io/en/stable/)|[https://pypi.org/project/marshmallow/](https://pypi.org/project/marshmallow/)|
|pywinrm|Python library for Windows Remote Management.|[https://github.com/diyan/pywinrm/](https://github.com/diyan/pywinrm/)|[https://pypi.org/project/pywinrm/](https://pypi.org/project/pywinrm/)|
|pytest|pytest: simple powerful testing with Python.|[https://docs.pytest.org/en/stable/](https://docs.pytest.org/en/stable/)|[https://pypi.org/project/pytest/](https://pypi.org/project/pytest/)|
### 2.1.1 Extras for Connexion Library
Connexion provides "extras" with optional dependencies (which are strongly recommended to be installed) to unlock additional features. Some are given below:
- **swagger-ui:** Enables a Swagger UI console for your application as being a part of OpenAPI/Swagger support.
- **uvicorn:** Enables to run the application using ``app.run()``, recommended for development, instead of using an external ASGI server.
- **flask:** Enables the FlaskApp to build applications compatible with the Flask ecosystem and converts Flask's WSGI app into an ASGI one which can be defined as exteded version of WSGI.
Specified libraries can be installed as follows:
```
pip install connexion[swagger-ui]
pip install connexion[uvicorn]
pip install connexion[flask]
```
### 2.1.2 Extras for PyWinRM library
To install pywinrm with support for basic, certificate, and NTLM auth it can be typed simply ``pip install pywinrm``.
To use Kerberos authentication the following optional dependencies are needed:
**for Debian/Ubuntu/etc:**
```
$ sudo apt-get install gcc python3-dev libkrb5-dev
$ pip install pywinrm[kerberos]
```
**for RHEL/CentOS/etc:**
```
sudo dnf install gcc krb5-devel krb5-workstation python3-devel
pip install pywinrm[kerberos]
```
To use CredSSP authentication optional dependencies must be installed:
```
pip install pywinrm[credssp]
```
## 2.2 Extra Libraries for Specific Needs
|Library|Explanation|Official Documentation|Pypi Page|
|--|--|--|--|
|pg8000|PostgreSQL interface library.|[https://github.com/tlocke/pg8000](https://github.com/tlocke/pg8000)|[https://pypi.org/project/pg8000/#description](https://pypi.org/project/pg8000/#description)|
|Flask-Cors|A Flask extension adding a decorator for CORS support|!--|[https://pypi.org/project/Flask-Cors/](https://pypi.org/project/Flask-Cors/)|
|paramiko|SSH2 protocol library.|[https://www.paramiko.org/](https://www.paramiko.org/)|[https://pypi.org/project/paramiko/](https://pypi.org/project/paramiko/)|