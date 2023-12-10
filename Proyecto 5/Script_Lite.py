import sqlite3
import pandas as pd

conn=sqlite3.connect('./data/Database.db')
cursor=conn.cursor()

df=pd.read_csv('./data/Archivo.csv',sep=';').reset_index(drop=True)
print(df)

df.to_sql('Persona', conn, index=False, if_exists='append')

cursor.close()
conn.close()