import requests  # I❤️ requests
from . import app

@app.task(name='respider')
def respider():
    start_spider_api = "http://iproxy:5666/api/start_spider/"
    request.get(start_spider_api)

