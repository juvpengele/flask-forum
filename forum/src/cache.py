import os
import json
from werkzeug.contrib.cache import FileSystemCache


class Cache:
    def __init__(self):
        cache_directory = os.path.join(os.getcwd(), 'forum', 'src', 'storage', 'cache')
        self.cache = FileSystemCache(cache_directory, default_timeout=10*60)

    def set(self, key, value, timeout=None):
       
        try:
            return self.cache.set(key, json.dumps(value), timeout=timeout)

        except Exception as exception:
            print("An error occured")


    def get(self, key):
        try:
            data = self.cache.get(key)

            if data:
                return json.loads(data)

        except Exception as exception:
            print(exception)


    def has(self, key):
        return self.cache.has(key) is not None
