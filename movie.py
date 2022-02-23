from msilib.schema import Error
import sqlite3
conn = sqlite3.connect('movies')

cur=conn.cursor
def sqlconn():
    try:
        con = sqlite3.connect('movies')
        print("Connection is created")
    except Error:
        print(Error)

#create database movies
tableQuery = ''' CREATE TABLE MOVIE(
                NAME TEXT,
                ACTOR TEXT,
                ACTRESS TEXT,
                DIRECTOR TEXT,
                YEAROFRELEASE TEXT)'''

#conn.execute(tableQuery)

#insart record
insertRecord = '''INSERT INTO MOVIE(NAME , ACTOR , ACTRESS , DIRECTOR , YEAROFRELEASE)
VALUES ('OM_SHANTI_OM','SHAH_RUKH_KHAN','DEEPIKA_PADUKON','FARAH_KHAN', 2007 )'''

conn.execute(insertRecord)

#show record
statement = '''SELECT * FROM MOVIE'''

conn.execute(statement)

print("All the data")
output = cur.fetchall()
for row in output:
    print(row)

conn.commit()




