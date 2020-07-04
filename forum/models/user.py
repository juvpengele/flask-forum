from flask_login import UserMixin
from forum import db
from . import ModelMixin


class User(db.Model, UserMixin, ModelMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    email_verified_at = db.Column(db.DateTime, nullable=True, default=None)
    confirmation_token = db.Column(db.String(200), nullable=True, default=None)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    threads = db.relationship("Thread", back_populates="owner")

    @classmethod
    def create(Cls, **kwargs):
        user = Cls(**kwargs)
        user.commit()

        return user