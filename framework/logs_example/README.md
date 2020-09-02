
# 1. Django development server

1. Run server: `python manage.py runserver`

2. Execute `curl localhost:8000/myapp/index` to see output in console:

```log
Print `myapp.views`
APP: 10116 - 2020-08-31 17:48:24,962 - myapp.views - INFO - Info
APP: 10116 - 2020-08-31 17:48:24,962 - myapp.views - WARNING - Warning
APP: 10116 - 2020-08-31 17:48:24,962 - myapp.views - CRITICAL - Critical
APP: 10116 - 2020-08-31 17:48:24,963 - myapp.views - ERROR - handled exception
Traceback (most recent call last):
  File "/Users/che/Projects/Tutors/logs/framework/logs_example/myapp/views.py", line 17, in index
    1/0
ZeroDivisionError: division by zero
====================
SERVER: INFO 31/Aug/2020 17:48:24,963 basehttp 10116 123145534590976 "GET /myapp/index HTTP/1.1" 200 5
```

3. Execute `curl localhost:8000/myapp/error` to see output in console:

```log
Internal Server Error: /myapp/error
Traceback (most recent call last):
  File "/Users/che/Projects/Tutors/logs/venv/lib/python3.8/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/Users/che/Projects/Tutors/logs/venv/lib/python3.8/site-packages/django/core/handlers/base.py", line 179, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/Users/che/Projects/Tutors/logs/framework/logs_example/myapp/views.py", line 26, in error
    1/0
ZeroDivisionError: division by zero
SERVER: ERROR 31/Aug/2020 17:54:39,433 basehttp 10116 123145534590976 "GET /myapp/error HTTP/1.1" 500 57922
```

# 2. Uwsgi server

1. Run uwsgi http-server: `cd framework && uwsgi ./logs_example/conf/uwsgi.ini`

2. Execute `curl localhost:8000/myapp/index` to see output in console:
```log
Print `myapp.views`
APP: 3716 - 2020-09-02 16:45:05,707 - myapp.views - INFO - Info
APP: 3716 - 2020-09-02 16:45:05,707 - myapp.views - WARNING - Warning
APP: 3716 - 2020-09-02 16:45:05,707 - myapp.views - CRITICAL - Critical
APP: 3716 - 2020-09-02 16:45:05,708 - myapp.views - ERROR - handled exception
Traceback (most recent call last):
  File "./myapp/views.py", line 17, in index
    1/0
ZeroDivisionError: division by zero
====================
UWSGI: [pid: 3716] 127.0.0.1 {28 vars in 326 bytes} [Wed Sep  2 16:45:05 2020] GET /myapp/index => generated 5 bytes in 14 msecs (HTTP/1.1 200) 5 headers in 164 bytes (1 switches on core 0)
```

3. Execute `curl localhost:8000/myapp/error` to see output in console:
```log
Internal Server Error: /myapp/error
Traceback (most recent call last):
  File "/Users/che/Projects/Tutors/logs/venv/lib/python3.8/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/Users/che/Projects/Tutors/logs/venv/lib/python3.8/site-packages/django/core/handlers/base.py", line 179, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "./myapp/views.py", line 26, in error
    1/0
ZeroDivisionError: division by zero
UWSGI: [pid: 3716] 127.0.0.1 {28 vars in 326 bytes} [Wed Sep  2 16:45:21 2020] GET /myapp/error => generated 52393 bytes in 40 msecs (HTTP/1.1 500) 6 headers in 186 bytes (2 switches on core 0)
```

# 3. Docker (Django + Uwsgi)

1. Build image: 

    `$ cd framework/logs_example`

    `$ docker build -t django_log .`

2. Run container:

    `$ docker run -p 8000:8000 --name django_log --rm django_log`

3. Execute `curl localhost:8000/myapp/index` and `curl localhost:8000/myapp/error` to see the same output as in (#2. Uwsgi server)

4. Stop container:

    `$ docker stop django_log`