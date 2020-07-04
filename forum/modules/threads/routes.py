from flask import redirect, url_for, flash, Blueprint, render_template
from flask_login import login_required, current_user
from slugify import slugify
from .forms import ThreadCreationForm
from forum.models import Thread

thread_blueprint = Blueprint("threads", __name__, template_folder="templates")


@thread_blueprint.route("/create", methods=["GET", "POST"])
@login_required
def create():
    thread_form = ThreadCreationForm()

    if thread_form.validate_on_submit():
        title = thread_form.title.data
        category_id = thread_form.category_id.data
        content = thread_form.content.data
        user_id = current_user.id

        thread = Thread(title=title, category_id=category_id, content=content, user_id=user_id, slug=slugify(title))
        thread.save()

        flash("Your question has been posted successfully", "success")
        return redirect(url_for("main.index"))

    return render_template("threads/create.html", form=thread_form)


