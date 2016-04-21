import logging
from app import app, db, models, lm, LoginManager
from flask import render_template, request, redirect, url_for, g
from flask.ext.login import login_user, current_user, logout_user, login_required
from .forms import SignupForm, LoginForm
from .models import User


@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    else:
        return render_template('index.html')


@app.route('/foodshops/<adress>')
def foodshops(adress):
    return render_template('foodshops.html', adress=adress)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = SignupForm(request.values)
    
    if request.method == 'POST':
        if form.validate():
            user = models.User(username=form.username.data, password=form.password.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
            
            login_user(user)
            
            return render_template('home.html', user=current_user)
        else:
            return render_template('signup.html', form=form)
    elif request.method == 'GET':
        return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm(request.values)

    if request.method == 'POST':
        if form.validate():
            user = User.query.filter_by(username=form.username.data.lower()).first()

            login_user(user)

            return render_template('home.html', user=current_user)
        else:
            return render_template('login.html', form=form)
    elif request.method == 'GET':
        return render_template('login.html', form=form)


@app.route('/cms')
def cms():
    return render_template()


@app.route('/logout')
def logout():
    logout_user()

    return redirect(url_for('index'))


@app.route('/home')
@login_required
def home():
    return render_template('home.html', user=current_user)


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@lm.unauthorized_handler
def unauthorized():
    return redirect(url_for('index'))
