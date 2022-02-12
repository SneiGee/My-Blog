from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from shareideas import db
from shareideas.models import Post
from shareideas.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route('/post/new-post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        bpost = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(bpost)
        db.session.commit()
        flash('Your post has been posted', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form, legend='Create Post')


@posts.route('/post/<int:post_id>')
def post(post_id):
    bpost = Post.query.get_or_404(post_id)
    return render_template('post.html', title=bpost.title, post=bpost)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    bpost = Post.query.get_or_404(post_id)
    if bpost.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        bpost.title = form.title.data
        bpost.content = form.content.data
        db.session.commit()
        flash('Your post has been updated', 'success')
        return redirect(url_for('posts.post', post_id=bpost.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@posts.route('/post/<int:post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    bpost = Post.query.get_or_404(post_id)
    if bpost.author != current_user:
        abort(403)
    db.session.delete(bpost)
    db.session.commit()
    flash('Your post has been deleted', 'success')
    return redirect('home')
