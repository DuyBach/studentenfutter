from app import db


class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    admin = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=True)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
        
    def check_password(self, password):
        if password == self.password:
            return True

        return False

    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class Foodshop(db.Model):
    __tablename__ = 'foodshop'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    # location = create new address
    # picture = images saved unter static/foodshop/*
    # price_range = $ under 5€ $$ under 9€ $$$ big money maker
    # rating = 1-5 stars with half
    # commentes = relationship

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Foodshop %r>' % self.name