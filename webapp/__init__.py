import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from webapp.dbmodel import User

app = Flask(__name__)

module_dir = os.path.dirname(os.path.abspath(__file__))
app.config['SECRET_KEY'] = '6567e0baf8ab4fbe8894bacf510034a2'
app.config['JSON_AS_ASCII'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:<sp>@localhost/wordmodeling"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///wordmodel.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ['mail']
app.config['MAIL_PASSWORD'] = os.environ['password']
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
mail = Mail(app)

dbfiles = os.path.join(module_dir, 'dbfiles')

if os.path.exists(dbfiles):
    print("dbfiles Exists")
else:
    os.mkdir(dbfiles)


# try:
import webapp.routes
# except Exception:
    # print("Route Exception : ", Exception)

try:
    from webapp.dbmodel import db
    db.init_app(app)
except Exception:
    print("Db error", Exception)


@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        print("this is userd ", user_id)
        return User.query.get(user_id)
    return None
