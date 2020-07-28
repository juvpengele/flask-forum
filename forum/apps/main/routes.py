from flask import Blueprint, render_template
from forum.database.models.thread import Thread
from sqlalchemy.orm import joinedload

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def index():
    threads = Thread.query.order_by(Thread.created_at.desc())\
                    .options(joinedload(Thread.category))\
                    .all()
    return render_template('main/index.html', threads=threads)


@main_blueprint.route('/about-us')
def about():
    return render_template('main/about-us.html')