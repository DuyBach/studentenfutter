import os


WTF_CSRF_ENABLE = True
SECRET_KEY = '\xa4\x93Q\xf1q2\x02J\xec;\xdd\xf7\xe3(\xb6\x92;\xbd\x8e\xdf\xd3\x10N\x03'

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:studentenfutter@localhost/studentenfutter'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')