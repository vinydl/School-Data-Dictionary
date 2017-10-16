from flask import render_template,session, request, redirect, url_for
from app import app,parsedd
import os
from werkzeug import secure_filename

ALLOWED_EXTENSIONS = set(['xls', 'xlsx'])
app.config['UPLOAD_FOLDER'] = "D:\\Users\\vinayaka.d\\Desktop\\Python projects\\SchoolDict\\Parse\\app\\upload"
#File extension checking
def allowed_filename(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
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