from celery import Celery

app = Celery(broker='redis://@redis1:6388/0', backend='redis://@redis1:6388/1')
app.config_from_object('taskq.config')
