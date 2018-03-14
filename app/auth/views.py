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
        flash(u'用户名或密码错误')
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
            flash(u'新密码更改成功')
            return redirect(url_for('main.profile', username=current_user.name))
        else:
            flash(u'密码填写错误')
    return render_template("change_password.html", form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'登出成功')
    return redirect(url_for('auth.login'))
