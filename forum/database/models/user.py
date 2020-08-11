from flask_login import UserMixin
from forum import db
from flask import Markup
from . import Base


class User(Base, UserMixin):
    __tablename__ = "users"
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    email_verified_at = db.Column(db.DateTime, nullable=True, default=None)
    confirmation_token = db.Column(db.String(200), nullable=True, default=None)
    
    threads = db.relationship("Thread", back_populates="owner")
    comments = db.relationship("Comment", back_populates="owner")

    @classmethod
    def create(cls, **kwargs):
        user = cls(**kwargs)
        user.save()

        return user

    def json_attributes(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name
        }
