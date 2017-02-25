#coding: utf-8

from datetime import timedelta
# celery
task_serializer = 'json'
beat_schedule = {  # celery beat 定时任务
    'respider_every_30_minutes': {
        'task': 'respider',
        'schedule': timedelta(seconds=30*60)
    },
}
# iproxy api root path
# root_path=""
# 爬取IP数目
ip_all=100
# 可用IP数目
ip_use=10
