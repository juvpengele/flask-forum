from flask import Blueprint, jsonify, request, abort
from flask_login import current_user, login_required
from forum.database.models import Thread, Comment
from forum.src.api.comment_schema import comments_schema, comment_schema
from forum.src.utilities.helpers import now
from forum.src.api.comment_schema import comment_validation_schema
from marshmallow import ValidationError


comments_blueprint = Blueprint("comments", __name__)


@login_required
@comments_blueprint.route('/threads/<int:thread_id>/comments', methods=["GET", "POST"])
def index(thread_id):
    thread = Thread.query.get_or_404(thread_id)

    if request.method == "POST":
        try:
            comment_validation_schema.load(request.json)
        except ValidationError as err:
            return jsonify(err.messages), 400

        comment = Comment(content=request.json["content"], user_id=current_user.id, thread_id=thread.id)
        comment.save()

        thread.increment("comments_count")

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

    if request.method == "PATCH":
        comment.update({
            "content": request.json["content"],
            "updated_at": now()
        })

        return jsonify(comment_schema.dump(comment)), 200
