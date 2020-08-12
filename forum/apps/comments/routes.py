from flask import Blueprint, jsonify, request
from flask_login import current_user
from forum.database.models import Thread, Comment
from forum.src.api.comment_schema import comments_schema, comment_schema


comments_blueprint = Blueprint("comments", __name__)


@comments_blueprint.route('/threads/<int:thread_id>/comments', methods=["GET", "POST"])
def index(thread_id):
    thread = Thread.query.get_or_404(thread_id)

    if request.method == "POST":
        comment = Comment(content=request.json["content"], user_id=current_user.id, thread_id=thread.id)
        comment.save()

        return jsonify(comment_schema.dump(comment)), 201

    else:
        comments = Comment.query.filter_by(thread_id=thread.id)\
                                .order_by(Comment.created_at.desc())\
                                .all()
        return jsonify(comments_schema.dump(comments)), 200


@comments_blueprint.route('/comments/<int:comment_id>', methods=["GET", "PATCH", "DELETE"])
def show(comment_id):
    comment = Comment.query.get_or_404(comment_id)

    if not comment.is_owner(current_user):
        return jsonify({"message": "You are not authorized to perform this action"}), 403

    if request.method == "DELETE":
        comment.delete()
        return jsonify([]), 204

