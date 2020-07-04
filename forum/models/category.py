from forum import db
from forum.models import ModelMixin
from forum.utilities.helpers import now


class Category(db.Model, ModelMixin):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=now)
    updated_at = db.Column(db.DateTime)

    threads = db.relationship("Thread", back_populates="category")
