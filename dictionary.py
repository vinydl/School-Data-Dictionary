from app import app
from app import parsedd
from app import db
import flask_admin as admin
from flask_admin.contrib.sqla import ModelView


# we have to import the models so that sqlalchemy can detect them and create the db
# how else would it know what to create ?
from app.admin.models import *

# creates the database
db.create_all()

admin = admin.Admin(app, name='School Data Dictionary', template_mode='bootstrap3')
admin.add_view(ModelView(CCSIZSET, db.session))
admin.add_view(ModelView(CONTROL, db.session))
admin.add_view(ModelView(HIGHDEG, db.session))
admin.add_view(ModelView(PREDDEG, db.session))
admin.add_view(ModelView(REGION, db.session))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
