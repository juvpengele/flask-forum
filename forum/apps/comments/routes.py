from flask import Blueprint, jsonify, request
from flask_login import current_user
from forum.database.models import Thread, Comment


comments_blueprint = Blueprint("comments", __name__)


@comments_blueprint.route('/threads/<int:thread_id>/comments', methods=["GET", "POST"])
def index(thread_id):
    thread = Thread.query.get_or_404(thread_id)

    if request.method == "POST" and current_user is not None:
        comment = thread.add_comment(content=request.content, owner=current_user)

        return jsonify(comment), 201

    comments = Comment.query.filter_by(thread_id=thread_id).all()
    serialized_comments = [comment.serialize() for comment in comments]

    return jsonify(serialized_comments), 200


