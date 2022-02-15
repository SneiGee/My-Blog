# My-Blog
My-Blog is a fully-featured blog built using Python, flaskr, SQLAlchemy, and more. It was forked from https://github.com/SneiGee/My-Blog and is still under development.  

## Install
To get started, download the project and follow the install steps below to either create a virtual environment for local development or use Docker to build and configure NGINX automatically along with the blog 

## Create virtual environment and run
```bash
python3.9 -m venv venv
. venv/bin/activate
``` 
After activating...
```bash
pip install --upgrade pip
pip install -e .
python run.py
``` 

## Build with Docker
```bash
docker-compose up -d
``` 

### Access
Open http://localhost:5000 if a virtual environment was used.
Open http://localhost if docker was used.

#### Clean-up
If a virtual environment was used, deactivate it.
```bash
deactivate
```

If Docker was used, shutdown the containers
```bash
docker stop flask nginx
```
