import pandas as pd
import sqlite3
#from .. import db

def parsexlsx(filename):
   schooldata = pd.read_excel(io=filename,sheetname='data_dictionary',parse_cols = "E:G")
   schvar = schooldata['VARIABLE NAME'].ffill()
   schooldata['VARIABLE NAME'] = schvar
   schfilter = schooldata.dropna(subset = ['VALUE','LABEL'], how='all')
   tablelist = ['CCSIZSET','CONTROL','HIGHDEG','PREDDEG','REGION']
   conn = sqlite3.connect('sqlite:///../schooldb.db')
   for eachval in tablelist:
     cur=conn.cursor()
     cur.execute('DELETE FROM '+eachval)
     conn.commit()
     temp =schfilter[schfilter['VARIABLE NAME']==eachval][['VALUE','LABEL']]
     temp.to_sql(eachval,conn, if_exists='append',index=False)
   conn.close