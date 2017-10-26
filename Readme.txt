How to include new tables(EX:REGION)?

1) app\admin\models.py

  * Create Class REGION(re use other class)

    class REGION(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    VALUE = db.Column(db.REAL())
    LABEL = db.Column(db.Text())

    
    def __init__(self, VALUE="", LABEL=""):
        self.VALUE = VALUE
        self.LABEL = LABEL
    
2) \app\parsedd.py

  * Update tablelist with REGION

     tablelist = ['CCSIZSET','CONTROL','HIGHDEG','PREDDEG','REGION']

3) dictionary.py

  * Add REGION VIEW(re use other)

    admin.add_view(ModelView(REGION, db.session))


URL Links:
CRUD URL: http://localhost:8000/admin/


Upload URL: http://localhost:8000/index