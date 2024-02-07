FROM python:3.10

ENV PYTHONUNBUFFERED 1
	PYTHONDONTWRITEBYTECODE 1

ADD requirements.txt /

RUN pip install -r /requirements.txt

WORKDIR /app