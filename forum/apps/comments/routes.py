from flask import Blueprint, jsonify, request
from flask_login import current_user
from forum.database.models import Thread


comments_blueprint = Blueprint("comments", __name__)


@comments_blueprint.route('/<string:thread_slug>/comments', methods=["GET","POST"])
def index(thread):
    thread = Thread.filter_by(slug=thread_slug).first_or_fail()

    if request == "POST" and current_user != None:
        comment = thread.add_comment(content=request.content, owner=current_user)

        return jsonify(comment), 201

    comments = thread.comments

    return jsonify(comments), 200


