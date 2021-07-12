FROM python:3.8
MAINTAINER manish_sharma1604@yahoo.com

RUN apt-get update -y && apt-get install zip && python3 -m venv /app
WORKDIR /app
COPY . /app/
EXPOSE 5000
RUN . /app/bin/activate && python3 -m pip install -r requirements.txt
ENTRYPOINT ["/bin/sh", "-c" , ". /app/bin/activate && python3 app.py"]