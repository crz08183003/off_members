import os
import xlrd
from flask_script import Shell, Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import User, Meetingtype, Grouptype

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

@manager.command
def readexcel():
    workbook = xlrd.open_workbook(r'./users.xlsx')
    sheet1 = workbook.sheet_by_index(0)
    cols = sheet1.col_values(0)
    for i in range(1, sheet1.nrows):
        stu_number=str(sheet1.cell(i, 1).value)
        check_user = User.query.filter_by(stu_number=stu_number).first()
        if check_user:
            pass
        else:
            user = User(name=str(sheet1.cell(i, 0).value),stu_number=stu_number,
                    password=str(sheet1.cell(i, 2).value))
            db.session.add(user)
            db.session.commit()

@manager.command
def initdb():
    db.create_all()

def make_shell_context():
    return dict(app=app, db=db, User=User, Meetingtype=Meetingtype, Grouptype=Grouptype)
manager.add_command("shell",
                    Shell(make_context=make_shell_context), use_ipython=True)
manager.add_command(
    "runserver",
    Server(port=(os.getenv('FLASK_PORT') or 5000), host='0.0.0.0'))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

