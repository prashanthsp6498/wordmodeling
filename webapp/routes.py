import webapp.userdatahandler as uhandler
from webapp import app
from webapp import mail
from webapp.dbmodel import db
from webapp.dbmodel import User
from webapp.forms import Registration, Login, ForgotPassword, PasswdRest
from webapp.languagemanager import LanguageManager
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from flask import url_for, session
from flask import render_template, request, jsonify, flash, redirect
from flask_login import login_user, logout_user, login_required
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash

langManager = LanguageManager()
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])


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
        return render_template("word_predictor.html",
                               filename=filename,
                               number=number)
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
            token = s.dumps(form.email.data, salt='email-confirm')
            msg = Message("Confirm Email", sender=app.config['MAIL_USERNAME'],
                          recipients=[form.email.data])
            link = url_for('confirm_email', token=token, _external=True)
            msg.body = 'Your link is {}'.format(link)
            print(msg.body)
            try:
                db.session.add(new_user)
                db.session.commit()
                uhandler.create_user_directory(hashed_email)
                mail.send(msg)
                flash("Verification link sent to your mail")
            except Exception:
                flash("User already exist")
                return render_template("register.html", form=form)
            return redirect(url_for('signin'))
        else:
            render_template("register.html", form=form)
    return render_template("register.html", form=form)


@app.route('/confirm_email/<token>', methods=['POST', 'GET'])
def confirm_email(token):
    try:
        email = s.loads(token, salt='email-confirm', max_age=600)
        print("EMAIL ", email)
        user = User.query.filter_by(email=email).first()
        if user:
            user.email_confirmation = True
            db.session.commit()
    except SignatureExpired:
        flash("Link is expired")
        return redirect(url_for('signin'))
    flash("Account Activated")
    return redirect(url_for('signin'))


@app.route('/', methods=['POST', 'GET'])
def signin():
    form = Login()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            print('user', user)
            if user:
                if user.email_confirmation:
                    if check_password_hash(user.password, form.password.data):
                        login_user(user)
                        uhandler.user_config['userhash'] = user.uuid
                        session['userdir'] = user.uuid
                        return redirect(url_for("dashboard"))
                    else:
                        flash("wrong password")
                        return render_template("login.html", form=form)
                else:
                    flash("First Confirm your Email")
                    return render_template("login.html", form=form)
            else:
                flash("User doesn't exist")
                return render_template("login.html", form=form)
            print(form.email.data)

    return render_template("login.html", form=form)


@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPassword()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user:
                token = s.dumps(form.email.data, salt='password-reset')
                msg = Message("Password Reset",
                              sender=app.config['MAIL_USERNAME'],
                              recipients=[form.email.data])
                link = url_for('reset_password', token=token, _external=True)
                msg.body = 'Your link is {}'.format(link)
                mail.send(msg)
                flash("Reset Link sent to your mail")
                return redirect(url_for("signin"))
            else:
                flash("User doesn't exist")
                return redirect(url_for("signin"))
    return render_template("forgotpassword.html", form=form)


@app.route('/reset_password/<token>', methods=['POST', 'GET'])
def reset_password(token):
    form = PasswdRest()
    try:
        email = s.loads(token, salt='password-reset', max_age=600)
        user = User.query.filter_by(email=email).first()
        if request.method == 'POST':
            if form.validate_on_submit():
                hashed_password = generate_password_hash(
                    form.password.data, method='sha256')
                user.password = hashed_password
                db.session.commit()
                flash("Password Reset Successfully")
                return redirect(url_for("signin"))
    except SignatureExpired:
        flash("Link is expired")
        return redirect(url_for('signin'))
    return render_template("resetpassword.html", form=form)


@app.errorhandler(404)
def not_found(error):
    return "<h1>Your imagination is beyond ours</h1>"


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
