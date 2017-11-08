from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()   # 数据库
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()  # 蓝本

from flask_login import LoginManager


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

from flask_mail import Mail

mail = Mail()       # 邮件

from flask_moment import Moment

moment = Moment()

from flask_admin import Admin, AdminIndexView

admin = Admin(index_view=AdminIndexView(
        name='导航栏',
        url='/admin'))



