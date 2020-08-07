from forum import ma
from .thread_schema import ThreadSchema
from .user_schema import UserSchema
from forum.database.models.comment import Comment


class CommentSchema(ma.SQLAlchemyAutoSchema):
    thread = ma.Nested(ThreadSchema)
    owner = ma.Nested(UserSchema)

    class Meta:
        model = Comment
        include_fk = True
        load_instance = True


comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)