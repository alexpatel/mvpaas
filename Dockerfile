FROM python:2.7

RUN pip install --upgrade pip && pip install \
    flask==0.10.1 \
    flask-admin==1.1.0 \
    flask-babel==0.9 \
    flask-assets==0.10 \
    flask-login==0.2.11 \
    flask-testing==0.6.2 \
    flask-script==2.0.5 \
    flask-sqlalchemy==2.0 \
    flask-wtf==0.11 \
    sqlalchemy==1.0.0

RUN apt-get -yqq update && apt-get install -yqq gunicorn

COPY ./web /app
COPY manage.py /manage.py

WORKDIR /app
EXPOSE 8082
RUN python /manage.py createdb
CMD ["/usr/bin/gunicorn", "--bind", "0.0.0.0:8082", "wsgi"]
