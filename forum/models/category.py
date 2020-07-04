from forum import db
from forum.models import Base


class Category(Base):
    __tablename__ = "categories"
    name = db.Column(db.String(100))
    slug = db.Column(db.String(200))

    threads = db.relationship("Thread", back_populates="category")
