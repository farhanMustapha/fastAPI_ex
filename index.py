import sqlite3

conn=sqlite3.connect("compta.db")
cur=conn.cursor()
req="""
CREATE TABLE IF NOT EXISTS quiz(
id INTEGER PRIMARY KEY AUTOINCREMENT,
question TEXT,
journal TEXT,
date Date,
compte_d TEXT,
compte_c TEXT,
montant_d TEXT,
montant_c TEXT
 )
"""
cur.execute(req)
conn.commit()
conn.close()


def ajouter_question():
    conn=sqlite3.connect("compta.db")
    cur=conn.cursor()
    cur.execute(
        '''
           INSERT INTO quiz (question ,journal ,date ,compte_d ,compte_c ,montant_d ,montant_c) values(?,?,?,?,?,?,?)
        '''
    )
    conn.commit()
    conn.close()
