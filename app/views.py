from app import app, db, models, lm, LoginManager
from flask import render_template, request, redirect, url_for, g
from flask.ext.login import login_user, current_user
from .forms import SignupForm
from .models import User


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/foodshops')
def foodshops():
    return render_template('foodshops.html')
    

@app.route('/signup', methods=['GET', 'POST'])
def signup():
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


'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()
'''


@app.route('/home')
def home():
    if g.user:
        render_template('home.html', user=g.user)
    
    redirect(url_for('index'))

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
