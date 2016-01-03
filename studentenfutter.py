import random
import string
import logging
from flask import Flask, render_template, request, url_for, redirect, abort, session
from flask_login import LoginManager
from models import db, User
from forms import SignupForm


app = Flask(__name__)

app.config.from_pyfile('config.py')
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == 'POST':
        app.logger.info(request.data)
        if not form.validate():
            return render_template('signup.html', form=form)
        else:
            app.logger.info('Test')
            # CREATE
            user = User(username=form.username.data, password=form.password.data, email=form.email.data)
            # SIGN IN
            # REDIRECT
            return redirect(url_for(index))
    elif request.method == 'GET':
        return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    pass


@app.route('/logout')
def logout():
    pass


def load_user(user_id):
    return User.get(user_id)


@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(400)


def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(32)])
    return session['_csrf_token']


app.jinja_env.globals['csrf_token'] = generate_csrf_token


if __name__ == '__main__':
    app.run(debug=True)
