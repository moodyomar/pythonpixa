FROM python:alpine
COPY . .
RUN pip3 install -r requirments.txt
CMD gunicorn --bind 0.0.0.0:3000 wsgi:app

MAINTAINER moodyomarz "contact@devmoody.com"