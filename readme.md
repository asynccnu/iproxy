# IPROXY

> 简单▄︻┻┳═一……爬虫代理池

## Environment Config

+ **config file**: container.env

```
# mongodb: 存储可用IP
MONOGO_HOST=127.0.0.1
MONOGO_PORT=27017
```

## IP Proxy Config

+ **config file**: taskq/config.py

```
beat_schedule = {  # celery beat 定时任务
    'respider_every_30_minutes': {
        'task': 'respider',
        'schedule': timedelta(seconds=time)  # 每个time(s)重新爬取IP
    },
}

# IP 爬虫部署URL
root_path="http://192.168.99.100:5666/"
# 每次爬取IP的数目
ip_all=100
# IP池中存储的可用IP数目
ip_use=10
```

## Deploy

```shell
$ docker-compose build && docker-compose stop && docker-compose up -d
$ docker-compose ps
$ docker-compose logs <container>
```

## Use

+ ```GET <root_path>/api/ip/````

![screen shot 2017-02-25 at 23 07 10](https://cloud.githubusercontent.com/assets/10671733/23332126/39b20c60-fbaf-11e6-995b-51caeb979868.png)


## Proxy List

+ http://cn-proxy.com/
