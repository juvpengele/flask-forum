from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_user, logout_user, login_required
from forum.apps.auth.form import RegistrationForm
from forum.apps.auth.form import LoginForm
from forum import bcrypt
from forum.database.models.user import User
from forum.src.utilities.functions import generate_random_str
from forum.src.utilities.helpers import now
from forum.src.mails.registration_mail import RegistrationMail


auth_blueprint = Blueprint('auth', __name__, template_folder='templates')


@auth_blueprint.route('/register', methods=["GET", "POST"])
def register():
    registration_form = RegistrationForm()

    if registration_form.validate_on_submit():
        name = registration_form.name.data
        email = registration_form.email.data
        password = bcrypt.generate_password_hash(registration_form.password.data).decode('utf-8')
        user = User.create(name=name,
                           email=email,
                           password=password,
                           confirmation_token=generate_random_str(length=50),
                           created_at=datetime.utcnow()
                           )

        registration_mail = RegistrationMail(recipient=user)
        registration_mail.send()

        flash("You have been registered successfully. Please valid your email", "success")
        return redirect(url_for("main.index"))

    return render_template('auth/register.html', form=registration_form)


@auth_blueprint.route('/register/confirmation/<string:token>')
def register_confirmation(token):

    user = User.query.filter_by(confirmation_token=token).first_or_404()
    
    user.update({
        "confirmation_token": None,
        "email_verified_at": now(),
        "updated_at": now()
    })

    login_user(user)

    return redirect(url_for("main.index"))


@auth_blueprint.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
                
        login_user(user)

        next = request.args.get('next')
        return redirect(next or url_for('main.index'))
        
    return render_template("auth/login.html", form=login_form)


@auth_blueprint.route('/logout', methods=["POST"])
@login_required
def logout():
    logout_user()

    flash("You are logged out successfully.", "success")
    return redirect(url_for('main.index'))
