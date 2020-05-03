import userdatahandler as uhandler
from flask import Flask, render_template, request, jsonify, flash, redirect
from flask import url_for, session
from flask_bootstrap import Bootstrap
from forms import Registration, Login
from languagemanager import LanguageManager
from flask_login import LoginManager, login_user, logout_user, login_required
# from flask_login import current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = '6567e0baf8ab4fbe8894bacf510034a2'
app.config['JSON_AS_ASCII'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:<sp>@localhost/wordmodeling"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)

try:
    from dbmodel import User, db
    db.init_app(app)
except Exception:
    print("Db error", Exception)

langManager = LanguageManager()


@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        print("this is userd ", user_id)
        return User.query.get(user_id)
    return None


@app.route('/editor')
@login_required
def editor():
    number = [0, 1, 2, 3, 4, 5, 6]
    return render_template('word_predictor.html', number=number)


@app.route('/api/wordpredict', methods=['GET'])
def wordpredict():
    global langManager
    text = request.args['word']
    text = text.split()[-1]
    suggestions = langManager.Suggestion(text)
    return jsonify(result=suggestions)


@app.route('/api/translator', methods=['GET'])
def getWord():
    global langManager
    word = request.args['word']
    word = langManager.Trans(word)
    return jsonify({"word": word})


@app.route('/dashboard', methods=['POST', 'GET'])
@login_required
def dashboard():
    files = uhandler.get_user_files(session['userdir'])
    if request.method == 'POST':
        filename = request.form['filename']
        uhandler.create_user_file(session['userdir'], request.form['filename'])
        number = [0, 1, 2, 3, 4, 5, 6]
        return render_template("word_predictor.html", filename=filename, number=number)
    return render_template("dashboard.html", files=files)


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = Registration()
    if request.method == 'POST':
        if form.validate_on_submit():
            hashed_password = generate_password_hash(
                form.password.data, method='sha256')
            hashed_email = generate_password_hash(
                form.email.data, method="sha256")
            new_user = User(first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            email=form.email.data,
                            password=hashed_password,
                            uuid=hashed_email)
            try:
                db.session.add(new_user)
                db.session.commit()
                uhandler.create_user_directory(hashed_email)
            except Exception:
                flash("User already exist")
                return render_template("register.html", form=form)
            return redirect(url_for('signin'))
        else:
            render_template("register.html", form=form)
    return render_template("register.html", form=form)


@app.route('/', methods=['POST', 'GET'])
def signin():
    form = Login()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            print('user', user)
            if user:
                if check_password_hash(user.password, form.password.data):
                    login_user(user)
                    uhandler.user_config['userhash'] = user.uuid
                    session['userdir'] = user.uuid
                    return redirect(url_for("dashboard"))
                else:
                    flash("wrong password")
                    return render_template("login.html", form=form)
            else:
                flash("User doesn't exist")
                return render_template("login.html", form=form)
            print(form.email.data)

    return render_template("login.html", form=form)

# @app.errorhandler(404)
# def not_found(error):
#     return "<h1>Ooooooooooppppppppssssssssssssss</h1>"


@app.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect(url_for("signin"))


@app.route('/api/files', methods=['GET'])
def files():
    filename = request.args['filename']
    data = uhandler.read_user_file(session['userdir'], filename)
    return jsonify({"filedata": data})

@app.route('/api/save_text', methods=['POST', 'GET'])
def save_text():
    if request.method == 'POST':
        filename = request.form['filename']
        if filename[-1] == '#':
            filename = filename[:-1]
        data = request.form['text']
        response = uhandler.save_to_file(session['userdir'], filename, data)
        return jsonify({"response": response})
    return "oooooopsss"

if __name__ == "__main__":
    app.run(debug=True)