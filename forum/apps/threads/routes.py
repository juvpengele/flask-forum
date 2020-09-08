from flask import redirect, url_for, flash, Blueprint, render_template, abort, request
from flask_login import login_required, current_user
from slugify import slugify
from .forms import ThreadCreationForm
from forum.database.models import Thread, Category
from forum.src.decorators.email_verified import email_verified
from sqlalchemy.orm import joinedload

thread_blueprint = Blueprint("threads", __name__, template_folder="templates")




@thread_blueprint.route("/create", methods=["GET", "POST"])
@login_required
@email_verified
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


@thread_blueprint.route("<string:category_slug>")
def category_threads(category_slug):
    category = Category.query.filter_by(slug=category_slug).first_or_404()

    page = request.args.get('page', 1, type=int)

    threads = Thread.query\
                    .filter_by(category_id=category.id)\
                    .order_by(Thread.created_at.desc())\
                    .options(joinedload(Thread.category))\
                    .options(joinedload(Thread.comments))\
                    .paginate(page, 10, False)

    return render_template('main/index.html', threads=threads)



@thread_blueprint.route("<string:category_slug>/<string:thread_slug>", methods=["GET", "POST", "DELETE", "PUT"])
def show(category_slug, thread_slug):
    category = Category.query.filter_by(slug=category_slug).first_or_404()
    thread = Thread.query\
        .filter_by(category_id=category.id, slug=thread_slug)\
        .first_or_404()

    if request.method == "GET":
        thread.update({"views_count": thread.views_count + 1})

    if request.method == b"DELETE":
        if thread.is_owner(current_user):
            thread.delete()
            flash("Your question has been deleted successfully", "success")

            return redirect(url_for('main.index'))
        else:
            abort(403)
        
    if request.method == b"PUT":
        if thread.is_owner(current_user):
            thread.update({
                "title": request.form['title'],
                "slug": slugify(request.form['title']),
                "category_id": request.form['category_id'],
                "content": request.form['content']
            })

            flash("Your question has been updated successfully", "success")

            return redirect(url_for('threads.show', category_slug=thread.category.slug, thread_slug=thread.slug))
        else:
            abort(403)

    return render_template("threads/show.html", thread=thread)


@thread_blueprint.route("<string:category_slug>/<string:thread_slug>/edit")
@login_required
@email_verified
def edit(category_slug, thread_slug):

    category = Category.query.filter_by(slug=category_slug).first_or_404()
    thread = Thread.query.filter_by(category_id=category.id, slug=thread_slug).first_or_404()

    if not thread.is_owner(current_user):
        abort(403)

    thread_form = ThreadCreationForm()

    thread_form.title.data = thread.title
    thread_form.category_id.data = thread.category_id
    thread_form.content.data = thread.content
    thread_form.submit.label.text = "Edit"

    return render_template("threads/edit.html", thread=thread, form=thread_form)
