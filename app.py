import os
from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for, request, g, jsonify, current_app, Markup
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from api import process_text


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = os.environ.get('FOR_DESNOS_ONLY', 'Testkey')
#sqlite_url = 'sqlite:///' + os.path.join(basedir, 'app.db')
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', sqlite_url)

Bootstrap(app)
CSRFProtect(app)

@app.route('/visualization', methods=['GET', 'POST'])
def text_output():
    if request.method == 'POST':    
        text = request.form.get('user-text') # validated on client
        proc = process_text(text)
        return render_template('output.html', 
            words=proc['words'],
            word_count=proc['word_count'],  
            dependencies=Markup(proc['svg']) # must be pre-sanitized
        )
    else: # GET
        return redirect(url_for('index'))

@app.route('/enjoin', methods=['GET'])
def enjoin():
    return render_template('input.html')

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('enjoin'))

