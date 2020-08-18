from flask import render_template, url_for, redirect, Blueprint
from flask_login import login_required

settings_blueprint = Blueprint("settings", __name__, template_folder="templates")

@login_required
@settings_blueprint.route("/")
def index():
    return render_template("settings/index.html")