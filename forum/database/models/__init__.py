from forum import db


class Base(db.Model):
    __abstract__ = True

    json_attributes = ()

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

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_json(self):
        attributes = {}

        for key in self.json_attributes:
            attributes[key] = getattr(self, key)

        return attributes

    def increment(self, column):
        column_value = getattr(self, column, 0)
        self.update({column: column_value + 1})



from .user import User
from .category import Category
from .thread import Thread
from .comment import Comment
