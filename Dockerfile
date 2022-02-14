FROM python:3.9-slim-buster

WORKDIR /python-docker
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN pip install --upgrade pip
RUN pip install -e .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
