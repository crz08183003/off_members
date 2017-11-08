from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()   # 数据库
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()  # 蓝本

from flask_login import LoginManager

login_manager = LoginManager()

from flask_mail import Mail

mail = Mail()       # 邮件

from flask_moment import Moment

moment = Moment()

from flask_admin import Admin

admin = Admin()

from flask_babelex import Babel

babel = Babel()

