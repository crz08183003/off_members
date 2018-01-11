from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, ValidationError, EqualTo, Email
from ..models import User
# 登录表单
class LoginForm(FlaskForm):
    stu_number = StringField('学号', validators=[DataRequired(), Length(8, 14)], render_kw={"style": "font-size: 5px"})
    password = PasswordField('密码', validators=[DataRequired()])
    # remember_me = BooleanField('记住我')
    submit = SubmitField('Log In')


# 修改密码表单
class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('旧密码', validators=[DataRequired()])
    password = PasswordField('新密码', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('确认新密码', validators=[DataRequired()])
    submit = SubmitField('修改密码')



class PasswordResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('New Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')

