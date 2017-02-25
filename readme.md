# IPROXY

> 爬虫代理池

## Environment Config

+ **config file**: container.env

    # mongodb: 存储可用IP
    MONOGO_HOST=127.0.0.1
    MONOGO_PORT=27017

## IP Proxy Config

+ **config file**: taskq/config.py

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
    
## Deploy

    $ docker-compose build && docker-compose stop && docker-compose up -d
    $ docker-compose ps
    $ docker-compose logs <container>

## Proxy List

+ http://cn-proxy.com/
