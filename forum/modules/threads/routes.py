from flask import redirect, url_for, flash, Blueprint, render_template
from flask_login import login_required


thread_blueprint = Blueprint("threads", __name__, template_folder="templates")


@login_required
@thread_blueprint.route("/")
def create():
    return render_template("threads/create.html")
