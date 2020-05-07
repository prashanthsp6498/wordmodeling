import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from webapp.dbmodel import User

app = Flask(__name__)

module_dir = os.path.dirname(os.path.abspath(__file__))
app.config['SECRET_KEY'] = '6567e0baf8ab4fbe8894bacf510034a2'
app.config['JSON_AS_ASCII'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:<sp>@localhost/wordmodeling"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)


try:
    import webapp.routes
except Exception:
    print("Route Exception : ", Exception)

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
