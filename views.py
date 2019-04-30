from myapp import app
from flask import render_template

@app.route('/')
@app.route('/index.html')
@app.route('/index')
def index():
    return render_template('index.html')
