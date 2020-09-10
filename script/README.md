# 1. Unstructured log: default Python `logging` (Docker)

1. Build image:
  - `docker build -t py_log_script .`

2. Run container in background:
  - `docker run -d --name py_log_script --rm py_log_script`

3. Check logs:
  - `docker logs py_log_script`

Terminal output:

```log
  Print
  1 - 2020-08-23 18:39:13,782 - __main__ - DEBUG - Debug
  1 - 2020-08-23 18:39:13,783 - __main__ - INFO - Info
  1 - 2020-08-23 18:39:13,783 - __main__ - WARNING - Warning
  1 - 2020-08-23 18:39:13,783 - __main__ - CRITICAL - Critical
  1 - 2020-08-23 18:39:13,783 - __main__ - ERROR - Handled exception
  Traceback (most recent call last):
      File "example.py", line 24, in <module>
        1/0
  ZeroDivisionError: division by zero
```


4. Redirect Docker output into file:
  - Comment line `# time.sleep(60)`.
  - Uncomment line `# Unhandled exception`.
  - Rebuild image with command #1
  - `docker run --name py_log_script --rm py_log_script &> example.log`
    
    Note that we use `&>` redirect to save in file both STDOUT and STDERR.

File output:
```log
───────┬─────────────────────────────────────────────────────────────────────────────────────
       │ File: example.log
───────┼─────────────────────────────────────────────────────────────────────────────────────
   1   │ Print
   2   │ 1 - 2020-08-23 18:41:34,532 - __main__ - DEBUG - Debug
   3   │ 1 - 2020-08-23 18:41:34,532 - __main__ - INFO - Info
   4   │ 1 - 2020-08-23 18:41:34,532 - __main__ - WARNING - Warning
   5   │ 1 - 2020-08-23 18:41:34,532 - __main__ - CRITICAL - Critical
   6   │ 1 - 2020-08-23 18:41:34,532 - __main__ - ERROR - Handled exception
   7   │ Traceback (most recent call last):
   8   │   File "example.py", line 24, in <module>
   9   │     1/0
  10   │ ZeroDivisionError: division by zero
  11   │ ====================
  12   │ Traceback (most recent call last):
  13   │   File "example.py", line 31, in <module>
  14   │     sqrt(-1)  # !Uncomment to see that unhandled exceptions will appear in STDERR
  15   │ ValueError: math domain error
───────┴─────────────────────────────────────────────────────────────────────────────────────
```

5. You can also take a look on Docker stateful logs of the container.
Containers are stateless, and the logs are stored on the Docker host in JSON files by default.
But only if you don't use `--rm` flag when container starts.
This flag automatically remove the container when it exits (as well as logs and anonymous volumes)

- Uncomment line `# time.sleep(60)`.
- Run container: `docker run -d --name py_log_script py_log_script`
- Copy <container_id> from command output: `docker ps`
- Check logs in JSON format of this container on host:
  `cat /var/lib/docker/containers/<container_id>/<container_id>-json.log`
  Pay attention that:
      - logs and handled exception are in STDOUT
      - unhandled exception is in STDERR
      - each line is JSON-line, but multiline output (e.g. stack trace) formed as separate records,
        which is inconvenient and incorrect

JSON file output:

```log
───────┬───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 306c20c7b976a06cf49df300bbf8639c172b8b1d0d8b3c4e8bb8f8c0cccd317c-json.log
───────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
   1   │ {"log":"Print\n","stream":"stdout","time":"2020-08-24T14:06:44.051727267Z"}
   2   │ {"log":"1 - 2020-08-24 14:06:44,051 - __main__ - DEBUG - Debug\n","stream":"stdout","time":"2020-08-24T14:06:44.051755203Z"}
   3   │ {"log":"1 - 2020-08-24 14:06:44,051 - __main__ - INFO - Info\n","stream":"stdout","time":"2020-08-24T14:06:44.051758586Z"}
   4   │ {"log":"1 - 2020-08-24 14:06:44,051 - __main__ - WARNING - Warning\n","stream":"stdout","time":"2020-08-24T14:06:44.051760858Z"}
   5   │ {"log":"1 - 2020-08-24 14:06:44,051 - __main__ - CRITICAL - Critical\n","stream":"stdout","time":"2020-08-24T14:06:44.051763034Z"}
   6   │ {"log":"1 - 2020-08-24 14:06:44,051 - __main__ - ERROR - Handled exception\n","stream":"stdout","time":"2020-08-24T14:06:44.051973
       │ 313Z"}
   7   │ {"log":"Traceback (most recent call last):\n","stream":"stdout","time":"2020-08-24T14:06:44.051982185Z"}
   8   │ {"log":"  File \"example.py\", line 24, in \u003cmodule\u003e\n","stream":"stdout","time":"2020-08-24T14:06:44.051984859Z"}
   9   │ {"log":"    1/0\n","stream":"stdout","time":"2020-08-24T14:06:44.051987337Z"}
  10   │ {"log":"ZeroDivisionError: division by zero\n","stream":"stdout","time":"2020-08-24T14:06:44.051989428Z"}
  11   │ {"log":"====================\n","stream":"stdout","time":"2020-08-24T14:06:44.051992382Z"}
  12   │ {"log":"Traceback (most recent call last):\n","stream":"stderr","time":"2020-08-24T14:06:44.05205322Z"}
  13   │ {"log":"  File \"example.py\", line 31, in \u003cmodule\u003e\n","stream":"stderr","time":"2020-08-24T14:06:44.052057884Z"}
  14   │ {"log":"    sqrt(-1)  # !Uncomment to see that unhandled exceptions will appear in STDERR\n","stream":"stderr","time":"2020-08-24T
       │ 14:06:44.052060356Z"}
  15   │ {"log":"ValueError: math domain error\n","stream":"stderr","time":"2020-08-24T14:06:44.052062609Z"}
───────┴───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
```

# 2. Structured log: `JSON-log-formatter` (Docker, Loki)

1. Run Loki environment from `/loki`, see `/loki/README.md`

2. Run script in container with Loki as log-driver:

```bash
$ docker run --log-driver loki --log-opt loki-url=http://localhost:3100/loki/api/v1/push --name py_log_script --rm py_log_script
```

3. See parsed JSON rows in Grafana dashboard: http://localhost:3000, see `/loki/README.md`, similar to:

```json
Print
{"extra_code": "De", "message": "Debug", "time": "2020-09-10T08:30:09.052853"}
{"extra_code": "In", "message": "Info", "time": "2020-09-10T08:30:09.053104"}
{"extra_code": "Wa", "message": "Warning", "time": "2020-09-10T08:30:09.053154"}
{"extra_code": "Cr", "message": "Critical", "time": "2020-09-10T08:30:09.053198"}
{"extra_code": "Ex", "message": "Handled exception", "time": "2020-09-10T08:30:09.053244", "exc_info": "Traceback (most recent call last):\n  File \"example.py\", line 24, in <module>\n    1/0\nZeroDivisionError: division by zero"}
Traceback (most recent call last):
  File "example.py", line 29, in <module>
    sqrt(-1)  # !Uncomment to see that unhandled exceptions will appear in STDERR
ValueError: math domain error
```
* `JSON-log-formatter` has Python 2/3 support