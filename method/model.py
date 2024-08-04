from flask_sqlalchemy import SQLAlchemy
from main  import app

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#  設置資料庫為sqlite3
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(pjdir, 'data_register.sqlite')
app.config['SECRET_KEY']='your key'