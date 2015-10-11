## AS-Manager

Task manager for distributing tasks to scraper and 3rd-party API workers.

## Uses

Celery is used to manage and schedule tasks by enqueing string messages in Redis queues that have workers waiting. Celerybeat schedule is set up to trigger game scraping spiders on Friday, Monday and Tuesday @ 3am.

## Tasks

```python
@app.task
def crawl_all():
```  
- Enqueue `'CRAWL ALL SPIDERS'`  in scraper queue - initalizes worker for scraping NFL player info, NFL team info, and NFL players' game and season total stats
  
```python
@app.task
def crawl_games():
```  
- Enqueue `'CRAWL ALL GAMES'`  in scraper queue - initalizes worker for scraping NFL players' game and season total stats
  
```python
@app.task
def get_trends():
```  
- Enqueue `'GET TRENDING PLAYERS'`  in trending queue - initalizes worker for creating trending NFL players list
