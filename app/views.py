from flask import render_template, request, redirect, url_for
from app import app
from .forms import SignupForm


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
            # CREATE
            # SIGN IN
            # REDIRECT
            # user = User(username=form.username.data, password=form.password.data, email=form.email.data)
            # app.logger.info(user)
            return redirect(url_for('index'))
        else:
            return render_template('signup.html', form=form)
    elif request.method == 'GET':
        return render_template('signup.html', form=form)