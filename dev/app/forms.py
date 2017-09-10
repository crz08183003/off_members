from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	studentid = StringField('学号', validators=[DataRequired(message='学号不能为空')])
	password = PasswordField('密码', validators=[DataRequired(message='密码不能为空')])
	remember_me = BooleanField('remember_me', default=False)