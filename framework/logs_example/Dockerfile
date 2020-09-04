FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8001

CMD uwsgi ./conf/uwsgi.ini --die-on-term