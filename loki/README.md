# Loki + Grafana

0. Run Django app with docker-compose from `framework/logs_example`, see `README.MD`

1. Run Loki and Grafana with docker-compose:
    
    ```bash
    $ cd loki/
    $ docker-compose up
    ```

2. Login into Grafana: 

    http://localhost:3000, `admin/admin`

3. Add Loki datasource: 

    - Open http://localhost:3000/datasources, `Add data source`
    
    - Select `Loki`, set `Name` = `Loki`, `Url` = `http://loki:3100`, `Save & Test`

4. Make a couple of requests: 

    - `$ curl localhost:8000/myapp/index`
    
    - `$ curl localhost:8000/myapp/error`

5. Open Grafana -> Explore http://localhost:3000/explore, select `Log labels/compose_service/web` and see app logs. 
