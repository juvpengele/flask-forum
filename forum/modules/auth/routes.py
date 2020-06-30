from flask import Flask, Blueprint, render_template, request, redirect, url_for
from forum.modules.auth.form import RegistrationForm

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')


@auth_blueprint.route('/register', methods=["GET", "POST"])
def register():
    registration_form = RegistrationForm()

    if registration_form.validate_on_submit():
        print("Validated")

        redirect(url_for("auth"))

    return render_template('auth/register.html', form=registration_form)