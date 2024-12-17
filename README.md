# 1. FOLDER/FILE STRUCTURE OF THE PROJECT

TSMProject
├── API # Backend logic of the project
│   ├── Alembic # Migration files will be created here
│   │   └── Version1.0 # Versioning
│   ├── Base
│   │   ├── Config
│   │   │   ├── __ini__.py
│   │   │   ├── Config.py
│   │   │   └── settings.toml
│   │   ├── DBService # Common DB helpers (e.g., to avoid code across services)
│   │   │   ├── __init__.py
│   │   │   ├── IDBService.py
│   │   │   └── IModel.py
│   │   ├── DependencyInjection
│   │   │   ├── __init__.py
│   │   │   ├── Container.py # Dependency Injection container
│   │   │   └── Interface.py # Abstract interfaces for DI
│   │   ├── Exceptions
│   │   │   ├── __init__.py
│   │   │   ├── AppExceptions.py # Custom application exceptions
│   │   │   └── ErrorHandlers.py # Global error handlers for Connexion
│   │   ├── Utils
│   │   │   ├── __init__.py
│   │   │   ├── AuthUtils.py # Authoriztion utilities
│   │   │   ├── IUtils.py # Abstract of utility functions
│   │   │   └── ValidationUtils.py # Input validation utilities
│   │   ├── __init__.py # Can contain shared logic (e.g., UUID models, common helpers
│   │   └── IService.py
│   ├── Services # Contains all the services and sub-services.
│   │   ├── AuthService
│   │   │   ├── __init__.py
│   │   │   ├── AuthService.py # Authentication logic (e.g., JWT)
│   │   │   ├── docker-compose.yaml
│   │   │   ├── openapi.yaml
│   │   │   ├── README.md
│   │   │   └── Routes.py
│   │   ├── DBService
│   │   │   ├── Models
│   │   │   │   ├── Role.py
│   │   │   │   ├── User.py
│   │   │   │   └── UserRole.py # Many to many relation between User and Role classes
│   │   │   ├── __init__.py
│   │   │   ├── DBService.py # DB configuration&migration processes (e.g., SQLAlchemy setup)
│   │   │   └── MigrationHelper.py # For database migrations (e.g., creating tables programmatically)
│   │   ├── LogService
│   │   │   ├── __init__.py
│   │   │   ├── docker-compose.yaml
│   │   │   ├── LogService.py # Custom logging configuration
│   │   │   ├── openapi.yaml
│   │   │   ├── README.md
│   │   │   └── Routes.py
│   │   ├── MailService
│   │   │   ├── __init__.py
│   │   │   ├── docker-compose.yaml
│   │   │   ├── MailService.py # Email logic (e.g., sending email)
│   │   │   ├── openapi.yaml
│   │   │   ├── README.md
│   │   │   └── Routes.py
│   │   ├── RoleService
│   │   │   ├── __init__.py
│   │   │   ├── docker-compose
│   │   │   ├── opeapi.yaml
│   │   │   ├── README.md
│   │   │   ├── RoleServic.py
│   │   │   └── Routes.py
│   │   ├── ScriptService
│   │   │   ├── Scripts
│   │   │   │   ├── ComputerHelper.ps1 # Active Directory computer processes (e.g., add computer, move computer)
│   │   │   │   ├── GenericHelper.ps1 # Generic processes (e.g., generate password, convervt PSObject to json)
│   │   │   │   ├── GroupHelper.ps1 # Active Directory group processes (e.g., create group)
│   │   │   │   ├── OUHelper.ps1 # Active Directory Organisational Unit processes
│   │   │   │   ├── RemoteHelper.ps1 # Helps to run all the AD processes remotely
│   │   │   │   └── UserHelper.ps1 # Active Directory user processes
│   │   │   ├── __init__.py
│   │   │   ├── docker-compose.yaml
│   │   │   ├── openapi.yaml
│   │   │   ├── README.md
│   │   │   ├── Routes.py
│   │   │   └── ScriptService.py # PowerShell script execution logic
│   │   └── UserService
│   │       ├── __init__.py
│   │       ├── docker-compose.yaml
│   │       ├── openapi.yaml
│   │       ├── README.md
│   │       ├── Routes.py
│   │       └── UserService.py # CRUD operations for DB objects (e.g., Users, UsersRoles)
│   ├── Tests
│   │   ├── E2E
│   │   ├── Integration
│   │   ├── Unit
│   │   └── Conftest.py
│   ├── Venv # Contains virtual environment folders&files
│   ├── .env # Contains environment variables
│   ├── .gitignore
│   ├── App.py # Startup file or main application file
│   ├── Dockerfile # Base image for the project (references each service's Dockerfile)
│   ├── README.md # Main project README file
│   └── requirements.txt # Contains the list of the dependencies
└── Web # Web frontend part of the application
    ├── Bootstrap # Bootstrap libraries, folders and files for visual side
    ├── index.html # Frontend startup file
    ├── Styles # Style output of the frontend
    │   └── style.css # Main css stylings
    └── Scripts # Contains js files which are responsible for consuming the API...
        └── Connect.js

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