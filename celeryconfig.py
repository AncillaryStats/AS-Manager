import os
from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = os.environ['RABBITMQ_BIGWIG_URL']

# Crawl game stats Friday, Monday, and Tuesday @ 3am
# Get trending players every hour
# Print test messag every minute
CELERYBEAT_SCHEDULE = {
    'get-stats-after-games': {
        'task': 'tasks.crawl_games',
        'schedule': crontab(hour=3, day_of_week='friday,monday,tuesday')
    },
    'get-trending-players': {
        'task': 'tasks.get_trends',
        'schedule': timedelta(seconds=3600)
    },
    'print-test-message': {
        'task': 'tasks.test_message',
        'schedule': timedelta(seconds=60),
    },
}


CELERY_TIMEZONE = 'US/Pacific'
