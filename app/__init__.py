import os
from flask import Flask
from werkzeug import secure_filename

#Flask object initialization
#app flask object has to be created before importing views below
#because it calls "import app from app"

ALLOWED_EXTENSIONS = set(['xls', 'xlsx'])

app = Flask(__name__)
from app import views
