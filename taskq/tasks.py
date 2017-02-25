import requests  # I❤️ requests
from . import app

@app.task(name='respider')
def respider():
    start_spider_api = "%sapi/start_spider/?ip_all=%s&ip_use=%s" % (app.conf.root_path, app.conf.ip_all, app.conf.ip_use)
    requests.get(start_spider_api)
