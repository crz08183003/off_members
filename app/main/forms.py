from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError
from ..models import User, Grouptype, Meetingtype
from ..extentions import db




class Ask_leaveForm(FlaskForm):
    # group_type = SelectField('组别', choices=[
    #     ('后端组', '后端组'),
    #     ('前端组', '前端组')
    # ])

    def group_query_factory():
        return [t.group for t in db.session.query(Grouptype).all()]

    def meeting_query_factory():
        return [t.meeting for t in db.session.query(Meetingtype).all()]

    def get_pk(obj):
        return obj

    group_type = QuerySelectField('组别', validators=[DataRequired()], query_factory=group_query_factory, get_pk=get_pk)
    # meeting_type = SelectField('会议类型', choices=[
    #     ('大例会', '大例会'),
    #     ('小组例会', '小组例会')
    # ])
    meeting_type = QuerySelectField('组别', validators=[DataRequired()], query_factory=meeting_query_factory, get_pk=get_pk)
    reason = StringField('请假原因', validators=[DataRequired(), Length(1, 64)], render_kw={"placeholder": "请输入精简有力的64字以内的请假理由 "})
    submit = SubmitField('提交')



class EditProfileForm(FlaskForm):
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


class EditProfileAdminForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role', coerce=int)
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')