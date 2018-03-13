from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length
from wtforms import ValidationError
from ..models import User, Grouptype, Meetingtype
from ..extentions import db


class Ask_leaveForm(FlaskForm):
    def group_query_factory():
        return [t.group for t in db.session.query(Grouptype).all()]

    def meeting_query_factory():
        return [t.meeting for t in db.session.query(Meetingtype).all()]

    def get_pk(obj):
        return obj

    group_type = QuerySelectField('组别', validators=[
                                  DataRequired()], query_factory=group_query_factory, get_pk=get_pk)
    meeting_type = QuerySelectField('会议类型', validators=[
                                    DataRequired()], query_factory=meeting_query_factory, get_pk=get_pk)
    reason = TextAreaField('请假原因', validators=[DataRequired(), Length(
        1, 64)], render_kw={"placeholder": "请输入精简有力的64字以内的请假理由 "})
    submit = SubmitField('提交')
