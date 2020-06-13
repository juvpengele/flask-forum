from flask import Flask, Blueprint, render_template


main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    return render_template('main/index.html')

@main_blueprint.route('/about-us')
def about():
    return render_template('main/about-us.html')