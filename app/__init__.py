from flask import Flask, request, flash, redirect, render_template, url_for, session
from config import config
from .admin import AskleaveModelView, MyView, MeetingModelView, GroupModelView
from flask_admin import Admin, AdminIndexView
from .extentions import (db, bootstrap, login_manager, moment, babel, admin)

login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)
    babel.init_app(app)
    admin.init_app(app, index_view=AdminIndexView(
        name=u'后台管理',
        template='admin_index.html',
        url='/YouGuess'
    ))

    admin.add_view(MyView(name='前台'))
    admin.add_view(AskleaveModelView(db.session, name=u'管理请假信息'))
    admin.add_view(MeetingModelView(db.session, name=u'管理会议名'))
    admin.add_view(GroupModelView(db.session, name=u'管理组名'))


    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app