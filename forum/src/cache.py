import os
import json
from werkzeug.contrib.cache import FileSystemCache


class Cache:
    def __init__(self):
        self._cache = FileSystemCache(Cache.cache_dir(), default_timeout=10*60)

    @staticmethod
    def cache_dir():
        return os.path.join(os.getcwd(), 'forum', 'src', 'storage', 'cache')

    def set(self, key, value, timeout=None):
        try:
            return self._cache.set(key, json.dumps(value), timeout=timeout)

        except Exception as exception:
            print(exception)


    def get(self, key):
        try:
            data = self._cache.get(key)
            if data:
                return json.loads(data)

        except Exception as exception:
            print(exception)


    def has(self, key):
        return self._cache.has(key) is not None
