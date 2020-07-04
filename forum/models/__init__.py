from forum import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def update(self, attributes):
        for key, value in attributes.items():
            setattr(self, key, value)
        self.save()

    def save(self):
        db.session.add(self)
        db.session.commit()


from .user import User
from .category import Category
from .thread import Thread
