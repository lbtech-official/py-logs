FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

RUN uwsgi --build-plugin /app/conf/escape_json.c

EXPOSE 8001

CMD uwsgi ./conf/uwsgi.ini --die-on-term