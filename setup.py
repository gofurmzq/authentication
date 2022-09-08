"""Installation script for flask-api-tutorial application."""
# 12 failed, 3 passed, 12 skipped, 25 warnings
from pathlib import Path
from setuptools import setup, find_packages

DESCRIPTION = (
    "Boilerplate Flask API with Flask-RESTx, SQLAlchemy, pytest, flake8, "
    "tox configured"
)
APP_ROOT = Path(__file__).parent
README = (APP_ROOT / "README.md").read_text()
AUTHOR = "Muhamad Gofur Muzaqi"
AUTHOR_EMAIL = "muhamadgofurmuzaqi@gmail.com"
PROJECT_URLS = {
    "Documentation": "https://github.com/gofurmzq/authentication",
    "Bug Tracker": "https://github.com/gofurmzq/authentication/issues",
    "Source Code": "https://github.com/gofurmzq/authentication",
}
INSTALL_REQUIRES = [
    "Flask",
    "Flask-Bcrypt==0.7.1",
    "Flask-Cors",
    "Flask-Migrate",
    "flask-restx",
    "Flask-SQLAlchemy",
    "PyJWT",
    "python-dateutil",
    "python-dotenv",
    "requests",
    "urllib3",
    "MarkupSafe==2.0.1",
    "Jinja2",
    "click==7.1.2",
    "werkzeug==0.16.1",
]
EXTRAS_REQUIRE = {
    "dev": [
        "black==21.4b0",
        "flake8==3.7.9",
        "pre-commit==2.9.2",
        "pydocstyle==5.0.2",
        "pytest==5.3.5",
        "pytest-black==0.3.8",
        "pytest-clarity==0.3.0a0",
        "pytest-dotenv==0.4.0",
        "pytest-flake8==1.0.4",
        "pytest-flask==0.15.1",
        "tox==3.14.5",
    ]
}

setup(
    name="flask-authentication",
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    version="0.1",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    license="MIT",
    url="https://github.com/gofurmzq/authentication",
    project_urls=PROJECT_URLS,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
)
