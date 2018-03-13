from flask import render_template, request, session, redirect, url_for, flash
from flask_login import login_required, current_user
from .forms import Ask_leaveForm
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
                              user_id=current_user.id,
                              actual_time=datetime.now())
        db.session.add(appli)
        return redirect(url_for('.profile', username=current_user.name))
    return render_template('ask_for_leave.html', form=form)

# 请假信息


@main.route('/profile/<username>', methods=['GET', 'POST'])
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


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
