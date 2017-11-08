from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin, AnonymousUserMixin
from datetime import datetime
from .extentions import db
from .extentions import login_manager, moment

class Asks_forleave(db.Model):
    __tablename__ = 'asks'
    id = db.Column(db.Integer, primary_key=True)
    leave_time = db.Column(db.DateTime(), default=datetime.utcnow())
    group = db.Column(db.String(32), index=True)
    type_of_meeting = db.Column(db.String(32), index=True)
    actual_time = db.Column(db.String(64), default=datetime.now())
    reason_for_leave = db.Column(db.String(128), index=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    stu_number = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(64))
    leave_applications = db.relationship(
        'Asks_forleave',
        backref='user',
        lazy='dynamic'
    )

    # 定义默认的用户角色
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    # hash 加密
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)

    def __repr__(self):
        return '<User %r>' % self.name


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))