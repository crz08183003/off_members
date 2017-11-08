from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask import render_template
from flask_login import current_user
from .models import Asks_forleave


class AskleaveModelView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.name == 'icbtbo':
            return True
        return False

    column_searchable_list = ('user.name', 'group', 'type_of_meeting')
    column_filters = ('user.name', 'group', 'type_of_meeting')
    can_create = False
    column_labels = {
        'id': u'序号',
        'user.name': u'姓名',
        'group': u'组别',
        'type_of_meeting': u'会议类型',
        'actual': u'请假时间',
        'reason_for_leave': u'请假原因'
    }
    column_list = ('id', 'user.name', 'group', 'type_of_meeting', 'actual_time', 'reason_for_leave')
    def __init__(self, session, **kwargs):
        super(AskleaveModelView, self).__init__(Asks_forleave, session, **kwargs)



class MyView(BaseView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.name == 'icbtbo':
            return True
        return False

    @expose('/', methods=['GET','POST'])
    def admin_index(self):
        return self.render('admin_index.html')