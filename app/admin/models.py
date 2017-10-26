from datetime import datetime

from .. import db


class CCSIZSET(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    VALUE = db.Column(db.REAL())
    LABEL = db.Column(db.Text())

    
    def __init__(self, VALUE="", LABEL=""):
        self.VALUE = VALUE
        self.LABEL = LABEL

class CONTROL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    VALUE = db.Column(db.REAL())
    LABEL = db.Column(db.Text())

    
    def __init__(self, VALUE="", LABEL=""):
        self.VALUE = VALUE
        self.LABEL = LABEL

class HIGHDEG(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    VALUE = db.Column(db.REAL())
    LABEL = db.Column(db.Text())

    
    def __init__(self, VALUE="", LABEL=""):
        self.VALUE = VALUE
        self.LABEL = LABEL

class PREDDEG(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    VALUE = db.Column(db.REAL())
    LABEL = db.Column(db.Text())

    
    def __init__(self, VALUE="", LABEL=""):
        self.VALUE = VALUE
        self.LABEL = LABEL

class REGION(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    VALUE = db.Column(db.REAL())
    LABEL = db.Column(db.Text())

    
    def __init__(self, VALUE="", LABEL=""):
        self.VALUE = VALUE
        self.LABEL = LABEL
                