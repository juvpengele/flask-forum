import os
from flask import render_template, url_for, redirect, Blueprint, request, flash, redirect, jsonify
from flask_login import login_required, current_user
from .form import AccountForm
from werkzeug.utils import secure_filename
from forum import app
from forum.src.utilities.functions import generate_random_str


settings_blueprint = Blueprint("settings", __name__, template_folder="templates")

@login_required
@settings_blueprint.route("/", methods=["GET", "POST"])
def index():
    account_form = AccountForm()

    if account_form.validate_on_submit():
        current_user.update({
            "name": account_form.name.data,
            "email": account_form.email.data
        })

        flash("Votre compte a été mis à jour avec succès", "success")

        return redirect(url_for("settings.index"))

    account_form.name.data = current_user.name
    account_form.email.data = current_user.email

    return render_template("settings/index.html", form=account_form)


@login_required
@settings_blueprint.route('/password', methods=["GET", "POST"])
def password():

    return render_template("settings/password.html")

@login_required
@settings_blueprint.route('avatar', methods=["POST"])
def avatar():

    avatar_file = request.files['avatar']

    filename = avatar_file.filename
    extension = filename.split(".")[-1]

    avatar_name = generate_random_str(20) + '.' + extension

    avatar_file.save(os.path.join(app.config['AVATAR_FOLDER'], avatar_name))

    current_user.update({
        "avatar": avatar_name
    })

    return jsonify({
        "avatar":  current_user.profile_picture
    })