import os

basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'asdAWdfz21zasdasdaw64!'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'site.bd')
SQLALCHEMY_TRACK_MODIFICATIONS = False
