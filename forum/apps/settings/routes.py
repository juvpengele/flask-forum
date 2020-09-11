import os
from flask import render_template, url_for, redirect, Blueprint, request, flash, redirect, jsonify
from flask_login import login_required, current_user
from .form import AccountForm, ChangePasswordForm
from werkzeug.utils import secure_filename
from forum import app
from forum.src.utilities.functions import generate_random_str
from forum.src.decorators.email_verified import email_verified
from forum.src.mails.registration_mail import send_validation_email
from forum import bcrypt


settings_blueprint = Blueprint("settings", __name__, template_folder="templates")

@settings_blueprint.route("/", methods=["GET", "POST"])
@login_required
def index():
    account_form = AccountForm()
    

    if account_form.validate_on_submit():
        email_changed = account_form.email.data != current_user.email

        current_user.update({
            "name": account_form.name.data,
            "email": account_form.email.data,
            "email_verified_at": None if email_changed else current_user.email_verified_at,
            "confirmation_token": generate_random_str(40) if email_changed else None
        })

        flash("Votre compte a été mis à jour avec succès", "success")
        
        if email_changed:
            flash("Your account has been disabled, you must validate your email", "warning")

            send_validation_email(current_user)

        return redirect(url_for("settings.index"))

    account_form.name.data = current_user.name
    account_form.email.data = current_user.email

    return render_template("settings/index.html", form=account_form)


@login_required
@settings_blueprint.route('/password', methods=["GET", "POST"])
def password():

    password_form = ChangePasswordForm()

    if password_form.validate_on_submit():
        current_user.update({
            "password": bcrypt.generate_password_hash(password_form.new_password.data)
        })

        flash("Your password has been changed successfully", "success")

        return redirect(url_for("settings.password"))

    return render_template("settings/password.html", form=password_form)


def _error_response(message, status_code = 422):
    return jsonify({
        "errors": {
            "avatar": message
        }
    }), status_code

avatar_extensions = ("png", "jpeg", "jpg", "gif") 

@login_required
@settings_blueprint.route('avatar', methods=["POST"])
def avatar():

    avatar_file = request.files['avatar']

    if not avatar_file:
        return _error_response("Please provide an image")

    extension = avatar_file.filename.split(".")[-1]

    if not extension or not extension in avatar_extensions: 
        return _error_response("Please provide a valid image")

    avatar_name = generate_random_str(20) + '.' + extension.lower()
    avatar_file.save(os.path.join(app.config['AVATAR_FOLDER'], avatar_name))

    current_user.update({ "avatar": avatar_name })

    return jsonify({
        "avatar":  current_user.profile_picture
    })

