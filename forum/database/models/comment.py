from . import Base
from forum import db


class Comment(Base):
    __tablename__ = "comments"

    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    owner = db.relationship("User", back_populates="comments")
