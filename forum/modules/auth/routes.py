from flask import Flask, Blueprint, render_template

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')


@auth_blueprint.route('/register')
def register():
    return render_template('auth/register.html')