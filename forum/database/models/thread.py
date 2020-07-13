from forum import db
from . import Base


class Thread(Base):
    __tablename__ = "threads"
    title = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(250), nullable=False)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    views_count = db.Column(db.Integer, nullable=False, default=0)

    owner = db.relationship("User", back_populates="threads")
    category = db.relationship("Category", back_populates="threads")

    @property
    def summary(self):
        return self.content[0:300] + "..."

    def is_owner(self, user):
        return user == self.owner
