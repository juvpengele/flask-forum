from sqlalchemy.ext.hybrid import hybrid_property

from forum import db
from . import Base
from .comment import Comment


class Thread(Base):

    json_attributes = ("id", "title", "slug", "content", "user_id", "category_id", "comments_count")

    __tablename__ = "threads"
    title = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(250), nullable=False)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    views_count = db.Column(db.Integer, nullable=False, default=0)
    comments_count = db.Column(db.Integer, default=0)
    best_comment_id = db.Column(db.Integer, nullable=True)

    owner = db.relationship("User", back_populates="threads")
    category = db.relationship("Category", back_populates="threads")
    comments = db.relationship("Comment", back_populates="thread")

    @property
    def summary(self):
        return self.content[0:300] + "..."

    def is_owner(self, user):
        return user == self.owner

    def add_comment(self, content, owner):
        comment = Comment(content=content, user_id=owner.id, thread_id=self.id)
        comment.save()

        return comment

    @hybrid_property
    def has_comments(self):
        return self.comments_count > 0

