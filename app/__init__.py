from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import flask_admin as admin
from flask_admin.contrib import sqla

from werkzeug import secure_filename
import os
from flask_admin.contrib.sqla import ModelView



app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdf129863dsfdsfadeqwezs'

ALLOWED_EXTENSIONS = set(['xls', 'xlsx'])
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'upload')
app.config.update(
        DEBUG=True,
        SQLALCHEMY_DATABASE_URI='sqlite:///../schooldb.db'
    )
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


 

#File extension checking
def allowed_filename(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        submitted_file = request.files['file']
        if submitted_file and allowed_filename(submitted_file.filename):
            filename = secure_filename(submitted_file.filename)
            #print(submitted_file.filename)
            #print(session['file'])
            
            submitted_file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            parsedd.parsexlsx(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            
    return render_template("index.html")

