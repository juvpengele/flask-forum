from flask import Blueprint, render_template, request
from forum.database.models.thread import Thread
from forum.database.models.comment import Comment
from sqlalchemy.orm import joinedload

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def index():

    threads = Thread.query\
        .options(joinedload(Thread.category))\
        .options(joinedload(Thread.comments))\

    page = request.args.get('page', 1, type=int)
    primary_filter = 'recent' if request.args.get('popular') is None else 'popular'

    if primary_filter == 'popular':
        threads = threads.order_by(Thread.views_count.desc())
    else:
        threads = threads.order_by(Thread.created_at.desc())

    secondary_filter = 'all' if request.args.get('filter') is None else request.args.get('filter')
    if secondary_filter is not None:
        if secondary_filter == 'answered':
            threads = threads.filter(Thread.comments_count > 0)

        if secondary_filter == 'unanswered':
            threads = threads.filter(Thread.comments_count == 0)

    threads = threads.paginate(page, 10, False)

    return render_template('main/index.html',
                           threads=threads,
                           primary_filter=primary_filter,
                           secondary_filter=secondary_filter
                           )


@main_blueprint.route('/about-us')
def about():
    return render_template('main/about-us.html')