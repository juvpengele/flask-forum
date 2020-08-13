from flask import Blueprint, render_template, request
from forum.database.models.thread import Thread
from sqlalchemy.orm import joinedload

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def index():
    page = request.args.get('page', 1, type=int)

    threads = Thread.query\
                    .order_by(Thread.created_at.desc())\
                    .options(joinedload(Thread.category))\
                    .options(joinedload(Thread.comments))\
                    .paginate(page, 10, False)

    return render_template('main/index.html', threads=threads)


@main_blueprint.route('/about-us')
def about():
    return render_template('main/about-us.html')