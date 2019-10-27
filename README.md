# Simple Catalog

## Installation
```bash
git clone git@github.com:Addovej/simple_catalog.git
cd simple_catalog
```
To build:
```bash
docker-compose build
```
To apply migrations:
```bash
docker-compose run app flask db upgrade
```
To create a superuser:
```bash
docker-compose run app flask create-superuser exampl@email.com
```
To launch
```bash
docker-compose up -d
```
To test code style
```bash
docker-compose run app flake8 app/
```

### Not docker installation
```bash
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
flask run
```


## Requirements
Python 3.6+

## Keywords
Flask, API, sqlalchemy, postgresql, flassger

### Background
It's just a test task
