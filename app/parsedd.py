import pandas as pd
import sqlite3

def parsexlsx(filename):
   schooldata = pd.read_excel(io=filename,sheetname='data_dictionary',parse_cols = "E:G")
   schvar = schooldata['VARIABLE NAME'].ffill()
   schooldata['VARIABLE NAME'] = schvar
   test = schooldata.dropna(subset = ['VALUE','LABEL'], how='all')
   conn = sqlite3.connect('schooldd.db')
   test.to_sql('collection',conn, if_exists='append')
   conn.close