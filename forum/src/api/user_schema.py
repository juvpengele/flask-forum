from forum import ma
from forum.database.models import User


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        fields = ("profile_picture", "name", "email")

    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
