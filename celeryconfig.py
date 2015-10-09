import os
from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = os.environ['RABBITMQ_BIGWIG_URL']

# Crawl game stats Friday, Monday, and Tuesday @ 3am
# CELERYBEAT_SCHEDULE = {
#     'get-stats-after-games': {
#         'task': 'tasks.crawl_games',
#         'schedule': crontab(hour=3, day_of_week='friday,monday,tuesday')
#     }
# }


CELERY_TIMEZONE = 'US/Pacific'
