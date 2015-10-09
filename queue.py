import os
import redis
r = redis.Redis.from_url(os.environ['REDISTOGO_URL'])

class RedisQueue(object):
    """Redis backed queue"""
    def __init__(self, name, db, namespace='queue'):
        self.__db=db
        self.key = '%s:%s' % (namespace, name)

    def is_empty(self):
        """If queue is empy, return True. Else, return False"""
        return self.__db.llen(self.key) == 0

    def enqueue(self, item):
        """Enqueue item into back of queue"""
        self.__db.rpush(self.key, item)

    def dequeue(self, block=True, timeout=None):
        """Dequeue front item from queue

        Args:
            block: (optiona) if queue is empty, blocks until can dequeue item
            timeout: (optional) timeout for blocking
        """
        if block:
            item = self.__db.blpop(self.key, timeout=timeout)
        else:
            item = self.__db.lpop(self.key)

        return item

scrapers = RedisQueue('scrapers', r)
trending = RedisQueue('trending', r)