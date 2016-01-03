from flask import Flask, render_template, request, url_for, redirect
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
        if not form.validate():
            return render_template('signup.html', form=form)
        else:
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


if __name__ == '__main__':
    app.run(debug=True)
