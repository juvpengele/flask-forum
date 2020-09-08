from flask import redirect, flash, url_for, request, jsonify
from functools import wraps
from flask_login import current_user

def email_verified(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        if current_user.email_verified_at is None:
            if request.is_xhr:
                return jsonify({
                    "errors": "You must validate your email"
                }), 403

            flash("You must validate your email", "warning")
            return redirect(url_for('main.index'))

        return f(*args, **kwargs)

    return decorated_function
