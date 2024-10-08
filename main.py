"""這個.py是在做路由轉換的以及資料前後端交換"""

from flask import Flask, render_template, request, jsonify
import logging
from method.logsetup import logsetup
from method.model_user import create_user

app = Flask(__name__) # __name__ 代表目前執行的模組
logsetup()
create_user()

@app.route('/')
def index():    
    """視圖函式 view function"""
    return "<p>Hello, World!</p>"


@app.route('/register',methods=['GET','POST'])
def register():
    form =FormRegister()
    if form.validate_on_submit():
        user = UserReister(
            username = form.username.data,
            email = form.email.data,
            password = form.password.data
        )
        db.session.add(user)
        db.session.commit()
        return 'Success Thank You'    
    return render_template('register.html')

@app.route('/login')
def login():
    
    return render_template('login.html')

if __name__ == '__main__':  
    app.debug = True
    app.run()

