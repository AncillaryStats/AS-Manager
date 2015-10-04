import os
import redis
from celery import Celery
from queue import RedisQueue

redis_url = os.environ['REDISTOGO_URL']

app = Celery('tasks')
app.config_from_object('celeryconfig')

scraper_q = RedisQueue('scrapers', redis_url)
trending_q = RedisQueue('trending', redis_url)

@app.task
def add(x, y):
    return x + y

@app.task
def crawl_all():
    scraper_q.enqueue('CRAWL ALL SPIDERS')

@app.task
def crawl_test():
    scraper_q.enqueue('CRAWL TEST MESSAGE')

@app.task
def get_trends():
    q.put('GET TRENDING PLAYERS')
