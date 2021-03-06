import os
from celery import Celery
import queue

app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task
def crawl_all():
    """
    Crawl all ESPN spiders - all player games, player info and team info
    """
    queue.scrapers.enqueue('CRAWL ALL SPIDERS')

@app.task
def crawl_games():
    """
    Crawl ESPN game stats
    """
    print('enqueueing message - CRAWL ALL GAMES @ scraper_q')
    queue.scrapers.enqueue('CRAWL ALL GAMES')

@app.task
def crawl_test():
    """
    Test message for crawling worker
    """
    queue.scrapers.enqueue('CRAWL TEST MESSAGE')

@app.task
def get_trends():
    """
    Get trending players via Reddit API
    """
    print('enqueueing message - GET TRENDING PLAYERS @ trending_q')
    queue.trending.enqueue('GET TRENDING PLAYERS')

@app.task
def test_message():
    """
    Print test message
    """
    print('Celery is running')

