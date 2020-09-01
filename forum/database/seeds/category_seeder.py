from forum.database.models.category import Category
from flask_seeder import Seeder
from slugify import slugify



category_names = ["PHP", "Javascript", "Python", "HTML-CSS"]


class CategorySeeder(Seeder):
    def run(self):
        for category_name in category_names:
            category = Category(name=category_name, slug=slugify(category_name))
            category.save()
