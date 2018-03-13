from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, redirect, url_for, request, flash, session
from . import auth
from .forms import LoginForm, ChangePasswordForm
from ..models import User
from .. import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(stu_number=form.stu_number.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(request.args.get('next') or url_for('main.ask_for_leave'))
        flash('Invalid username or password!')
    return render_template('login.html', form=form)




# 修改密码
@auth.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
   form = ChangePasswordForm()
   if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data
            db.session.add(current_user)
            flash('Your password has been updated.')
            return redirect(url_for('main.profile', username=current_user.name))
        else:
            flash('Invalid password.')
   return render_template("change_password.html", form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out!')
    return redirect(url_for('auth.login'))


#
# @auth.before_app_request
# def before_request():
#     if current_user.is_authenticated:
#         current_user.ping()
#         if not current_user.confirmed \
#                 and request.endpoint \
#                 and request.endpoint[:5] != 'auth.' \
#                 and request.endpoint != 'static':
#             return redirect(url_for('auth.unconfirmed'))
#
#
# @auth.route('/unconfirmed')
# def unconfirmed():
#     if current_user.is_anonymous or current_user.confirmed:
#         return redirect(url_for('main.index'))
#     return render_template('auth/unconfirmed.html')
#
# @auth.route('/confirm')
# @login_required
# def resend_confirmation():
#     token = current_user.generate_confirmation_token()
#     send_email(current_user.email, 'Confirm Your Account',
#                'auth/email/confirm', user=current_user, token=token)
#     flash('A new confirmation email has been sent to you by email.')
#     return redirect(url_for('main.index'))
#
#
#
#
# @auth.route('/secret')
# @login_required
# def secret():
#     return 'Only authenticated user are allowed!'