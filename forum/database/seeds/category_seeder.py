from flask_seeder import Seeder, generator
from forum.database.models import Category
from slugify import slugify


category_names = ["PHP", "Javascript", "Python", "HTML-CSS"]


class CategorySeeder(Seeder):
    def run(self):
        for category_name in category_names:
            category = Category(name=category_name, slug=slugify(category_name))
            category.save()
