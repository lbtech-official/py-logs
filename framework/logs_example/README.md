
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