import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logsetup import logsetup

logsetup()
#  取得目前文件資料夾路徑
pjdir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
#  新版本的部份預設為none，會有異常，再設置True即可。
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#  設置sqlite檔案路徑
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(pjdir, 'data.sqlite')

db = SQLAlchemy(app)

file = pjdir + '\data.sqlite'

class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.String(80), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

def create_user():
    if os.path.exists(file):
        logging.info("database already exists")
    else:   
        with app.app_context():
            db.create_all()
            logging.info("database isn't exists creating database")
create_user()
