from flask import Blueprint, jsonify, request
from flask_login import current_user
from forum.database.models import Thread, Comment
from forum.src.api.comment_schema import comments_schema


comments_blueprint = Blueprint("comments", __name__)


@comments_blueprint.route('/threads/<int:thread_id>/comments', methods=["GET", "POST"])
def index(thread_id):
    thread = Thread.query.get_or_404(thread_id)

    comments = Comment.query.filter_by(thread_id=thread.id).all()

    return jsonify(comments_schema.dump(comments)), 200


