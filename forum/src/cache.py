from werkzeug.contrib.cache import SimpleCache
import json

class Cache:
    def __init__(self):
        self.cache = SimpleCache()

    def set(self, key, value):
        try:
            self.cache.set(key, json.dumps(value))

        except Exception as exception:
            print("An error occured")


    def get(self, key):
        try:
            data = self.cache.get(key)

            print(data)

            if data:
                return json.loads(data)

        except Exception as exception:
            print(exception)


    def has(self, key):
        return self.cache.get(key) is not None
