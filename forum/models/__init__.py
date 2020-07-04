from forum import db


class ModelMixin:
    def update(self, attributes):
        for key, value in attributes.items():
            setattr(self, key, value)
        self.commit()

    def commit(self):
        db.session.add(self)
        db.session.commit()


from .user import User
from .category import Category
from .thread import Thread
