
# 1. Django development server

1. Run server: `$ python manage.py runserver`

2. Execute `$ curl localhost:8000/myapp/index` to see output in console:

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

3. Execute `$ curl localhost:8000/myapp/error` to see output in console:

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

1. Run uwsgi http-server: `$ cd framework && uwsgi ./logs_example/conf/uwsgi.ini`

2. Execute `$ curl localhost:8000/myapp/index` to see output in console:
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


  # 4. Docker (Django + Uwsgi + Nginx)

  1. Run bundle with docker-compose: 
      
      `$ cd framework/logs_example`

      `$ docker-compose up --build`

  2. Execute `$ curl localhost:8000/myapp/index` to see output in console:
```log
django_logs | Print `myapp.views`
django_logs | APP: 12 - 2020-09-04 17:20:55,107 - myapp.views - INFO - Info
django_logs | APP: 12 - 2020-09-04 17:20:55,107 - myapp.views - WARNING - Warning
django_logs | APP: 12 - 2020-09-04 17:20:55,107 - myapp.views - CRITICAL - Critical
django_logs | APP: 12 - 2020-09-04 17:20:55,107 - myapp.views - ERROR - handled exception
django_logs | Traceback (most recent call last):
django_logs |   File "./myapp/views.py", line 17, in index
django_logs |     1/0
django_logs | ZeroDivisionError: division by zero
django_logs | ====================
nginx_logs | NGINX: 172.19.0.1 - - [04/Sep/2020:17:20:55 +0000] "GET /myapp/index HTTP/1.1" 200 5 "-" "curl/7.64.1"rt=0.013 uct="0.000" uht="0.013" urt="0.013"
django_logs | UWSGI: [pid: 12] 172.19.0.1 {32 vars in 358 bytes} [Fri Sep  4 17:20:55 2020] GET /myapp/index => generated 5 bytes in 12 msecs (HTTP/1.1 200) 5 headers in 164 bytes (1 switches on core 0)
```

  3. Execute `$ curl localhost:8000/myapp/error` to see output in console:

```log
django_logs | Internal Server Error: /myapp/error
django_logs | Traceback (most recent call last):
django_logs |   File "/usr/local/lib/python3.8/site-packages/django/core/handlers/exception.py", line 47, in inner
django_logs |     response = get_response(request)
django_logs |   File "/usr/local/lib/python3.8/site-packages/django/core/handlers/base.py", line 179, in _get_response
django_logs |     response = wrapped_callback(request, *callback_args, **callback_kwargs)
django_logs |   File "./myapp/views.py", line 26, in error
django_logs |     1/0
django_logs | ZeroDivisionError: division by zero
django_logs | UWSGI: [pid: 10] 172.19.0.1 {32 vars in 358 bytes} [Fri Sep  4 17:21:20 2020] GET /myapp/error => generated 52772 bytes in 50 msecs (HTTP/1.1 500) 6 headers in 186 bytes (1 switches on core 0)
nginx_logs | NGINX: 172.19.0.1 - - [04/Sep/2020:17:21:20 +0000] "GET /myapp/error HTTP/1.1" 500 52772 "-" "curl/7.64.1"rt=0.051 uct="0.001" uht="0.051" urt="0.051"
```

# 5. Scale Django application

## 5.1 Scale with `docker-compose`

```bash
$ docker-compose up --scale web=3
```
- This will scale Django-application up to 3 instances. 

- You will see logs from `web_1`, `web_2`, `web_3` in Loki.

## 5.2 Scale with `docker stack`

1. In `Docker-desktop/Preferences/Kubernetes` enable options `Enable Kubernetes` and `Deploy Docker Stacks to Kubernetes by default`
2. Run stack in K8S cluster:
```bash
$ docker stack deploy --compose-file docker-compose.yaml django_log_k8_stack
```
*!!! PAY ATTENTION*: `docker stack` doesn't support `logging` section with logging drivers except of `json-file` and `journald`.
That is why you **won't see logs in Loki**.

PS: remove stack with `docker stack rm django_log_k8_stack`

## 5.3 Scale with Kubernetes

### 5.3.1 Setup environment

1. [Install](https://kubernetes.io/docs/tasks/tools/install-minikube/) and start `minikube`
2. [Install `helm`](https://helm.sh/docs/intro/install/)
3. [Install `Loki stack`](https://grafana.com/docs/loki/latest/installation/helm/): 
- Use `default` namespace. Because all the configs in `/k8s/*` use `default` namespace. 
- Use `--set grafana.enabled=true` flag
- Don't forget to `port-forward` Grafana to localhost

This will setup Loki/Grafana/Promtail in K8S (minikube) cluster.

4. Start `minikube` (if not started):
```bash
$ minikube start
```
5. Activate `Ingress` plugin for `minikube`:
```bash
$ minikube addons enable ingress
```
6. Start `dashboard` web interface:
```bash
$ minikube dashboard
```

### 5.3.2 Deploy Django application

```bash
$ cd framework/logs_example/k8s/
```

1. Create `Deployment` with 3 replicas:
```bash
$ kubectl apply -f deployment.yaml
```

2. Create `Service` with `NodePort` type:
```bash
$ kubectl apply -f deployment.yaml
```

3. Create `Ingress` with `nginx` controller:
```bash
$ kubectl apply -f ingress.yaml
```

4. Create `Configmap` for `Ingress`:
```bash
$ kubectl apply -f configmap.yaml
```
- Pay attention, that we use `nginx-load-balancer-conf` as `name` in `configmap.yaml`. This allows to automatically reload `Ingress` controller with new config after first upload or every time it changes. Please verify this name inside `kube-system` namespace in `Config and Storage/Config Maps` section inside minikube dashboard.

5. Inside minikube dashboard select `default` namespace and go to `Service/Ingresses`. Copy exposed IP of `nginx-ingress` in `Endpoints` column.


### 5.3.3 Request endpoints

1. Request with curl `<IP>/myapp/index` and `<IP>/myapp/error` several times and see structured JSON logs of app/uwsgi/nginx in Grafana http://localhost:3000
