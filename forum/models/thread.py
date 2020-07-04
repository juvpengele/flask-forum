from forum import db
from . import ModelMixin


class Thread(db.Model, ModelMixin):
    __tablename__ = "threads"
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_at = db.Column(db.DateTime)
    owner = db.relationship("User", back_populates="threads")

