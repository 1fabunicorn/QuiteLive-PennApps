from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html', title='QuiteLive Dashboard')

@app.route('/info')
def info():
    return render_template('info.html', title='About QuiteLive')
