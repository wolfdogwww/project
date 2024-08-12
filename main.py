"""這個.py是在做路由轉換的"""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__) # __name__ 代表目前執行的模組

@app.route('/')
def index():
    """視圖函式 view function"""
    return "<p>Hello, World!</p>"


@app.route('/register')
def register():
    
    return render_template('register.html')

@app.route('/login')
def login():
    
    return render_template('login.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
