from forum import ma
from forum.database.models import Thread


class ThreadSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Thread

    id = ma.auto_field()
    content = ma.auto_field()
    slug = ma.auto_field()
    views_count = ma.auto_field()
