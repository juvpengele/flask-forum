from forum import ma
from marshmallow import Schema, fields
from marshmallow.validate import Length
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


class CommentValidationSchema(Schema):
    content = fields.Str(required=True, validate=Length(min=2))


comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)
comment_validation_schema = CommentValidationSchema()
