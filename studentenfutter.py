from flask import Flask, render_template
from flask_login import LoginManager
from models import db, User

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
    pass


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
