import os
from flask_script import Shell, Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import User, Meetingtype, Grouptype
from importdata import read_excel


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Meetingtype=Meetingtype, Grouptype=Grouptype, read_excel=read_excel)
manager.add_command("shell",
                    Shell(make_context=make_shell_context), use_ipython=True)
manager.add_command(
    "startserver",
    Server(port=(os.getenv('FLASK_PORT') or 5000), host='0.0.0.0'))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

