from flask import render_template, request, session, redirect, url_for, flash
from flask_login import login_required, current_user
from .forms import EditProfileAdminForm, EditProfileForm, Ask_leaveForm
# from ..decorators import admin_required
from datetime import datetime
from . import main
from .. import db
from ..models import User, Asks_forleave



@main.route('/ask_for_leave', methods=['GET', 'POST'])
@login_required
def ask_for_leave():
    form = Ask_leaveForm()
    if form.validate_on_submit():
        appli = Asks_forleave(group=form.group_type.data,
                              type_of_meeting=form.meeting_type.data,
                              reason_for_leave=form.reason.data,
                              leave_time=datetime.utcnow(),
                              user_id=current_user.id)
        db.session.add(appli)
        return redirect(url_for('.profile', username=current_user.name))
    return render_template('ask_for_leave.html', form=form)

# 请假信息
@main.route('/profile/<username>', methods=['GET','POST'])
@login_required
def profile(username):
    user = User.query.filter_by(name=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    pagination = Asks_forleave.query.filter_by(user_id=user.id).order_by(db.desc(Asks_forleave.id)).paginate(
        page,
        per_page=10,
        error_out=False
    )
    apli = pagination.items
    return render_template('profile.html', applications=apli, pagination=pagination)

@main.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')
#
#
# @main.route('/user/<username>')
# def user(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     return render_template('user.html', user=user)
#
#
# @main.route('/edit-profile', methods=['GET', 'POST'])
# @login_required
# def edit_profile():
#     form = EditProfileForm()
#     if form.validate_on_submit():
#         current_user.name = form.name.data
#         current_user.location = form.location.data
#         current_user.about_me = form.about_me.data
#         db.session.add(current_user)
#         flash('Your profile has been updated.')
#         return redirect(url_for('.user', username=current_user.username))
#     form.name.data = current_user.name
#     form.location.data = current_user.location
#     form.about_me.data = current_user.about_me
#     return render_template('edit_profile.html', form=form)
#
#
# @main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
# @login_required
# @admin_required
# def edit_profile_admin(id):
#     user = User.query.get_or_404(id)
#     form = EditProfileAdminForm(user=user)
#     if form.validate_on_submit():
#         user.email = form.email.data
#         user.username = form.username.data
#         user.confirmed = form.confirmed.data
#         user.role = Role.query.get(form.role.data)
#         user.name = form.name.data
#         user.location = form.location.data
#         user.about_me = form.about_me.data
#         db.session.add(user)
#         flash('The profile has been updated.')
#         return redirect(url_for('.user', username=user.username))
#     form.email.data = user.email
#     form.username.data = user.username
#     form.confirmed.data = user.confirmed
#     form.role.data = user.role_id
#     form.name.data = user.name
#     form.location.data = user.location
#     form.about_me.data = user.about_me
#     return render_template('edit_profile.html', form=form, user=user)