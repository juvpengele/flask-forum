from flask import redirect, url_for, flash, Blueprint, render_template, abort, request
from flask_login import login_required, current_user
from slugify import slugify
from .forms import ThreadCreationForm
from forum.database.models import Thread, Category

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

        thread = Thread(title=title,
                        category_id=category_id,
                        content=content,
                        user_id=user_id,
                        slug=slugify(title),
                        views_count=0
                        )
        thread.save()

        flash("Your question has been posted successfully", "success")
        return redirect(url_for("main.index"))

    return render_template("threads/create.html", form=thread_form)


@thread_blueprint.route("<string:category_slug>/<string:thread_slug>", methods=["GET", "POST", "DELETE"])
def show(category_slug, thread_slug):
    category = Category.query.filter_by(slug=category_slug).first_or_404()
    thread = Thread.query.filter_by(category_id=category.id, slug=thread_slug).first_or_404()

    if request.method == "GET":
        thread.update({"views_count": thread.views_count + 1})

    if request.method == b"DELETE":
        if thread.is_owner(current_user):
            thread.delete()
            flash("Votre question a été supprimée avec succès", "success")

            return redirect(url_for('main.index'))
        else:
            abort(403)
        

    return render_template("threads/show.html", thread=thread)


@thread_blueprint.route("<string:category_slug>/<string:thread_slug>/edit")
@login_required
def edit(category_slug, thread_slug):

    category = Category.query.filter_by(slug=category_slug).first_or_404()
    thread = Thread.query.filter_by(category_id=category.id, slug=thread_slug).first_or_404()

    if not thread.is_owner(current_user):
        abort(403)

    thread_form = ThreadCreationForm()

    return render_template("threads/edit.html", thread=thread, form=thread_form)
