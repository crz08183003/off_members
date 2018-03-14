from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

# 登录表单
class LoginForm(FlaskForm):
    stu_number = StringField('', validators=[DataRequired(), Length(8, 14)],render_kw={"placeholder": u"学号"})
    password = PasswordField('', validators=[DataRequired()],render_kw={"placeholder": u"密码"})

# 修改密码表单
class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('旧密码', validators=[DataRequired()])
    password = PasswordField('新密码', validators=[
        DataRequired(), EqualTo('password2', message=u'两次密码需一致')])
    password2 = PasswordField('确认新密码', validators=[DataRequired()])
    submit = SubmitField('确认修改')
