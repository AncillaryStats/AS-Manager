import os
import redis
from celery import Celery
from queue import RedisQueue

redis_url = os.environ['REDISTOGO_URL']
r = redis.Redis.from_url(redis_url)

app = Celery('tasks')
app.config_from_object('celeryconfig')

scraper_q = RedisQueue('scrapers', r)
trending_q = RedisQueue('trending', r)

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
def dirs_test():
    scraper_q.enqueue('PRINT DIRS')

@app.task
def get_trends():
    trending_q.enqueue('GET TRENDING PLAYERS')
