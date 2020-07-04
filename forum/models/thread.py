from forum import db
from . import Base


class Thread(Base):
    __tablename__ = "threads"
    title = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(250), nullable=False)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    owner = db.relationship("User", back_populates="threads")
    category = db.relationship("Category", back_populates="threads")

