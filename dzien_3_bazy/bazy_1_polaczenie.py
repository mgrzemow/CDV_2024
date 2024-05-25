import sqlite3

# dbapi2.0

sql1='''
CREATE TABLE IF NOT EXISTS customer (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                age INTEGER,
                telephone TEXT,
                email TEXT,
                address TEXT
             )'''


conn = sqlite3.connect(':memory:')
# conn = sqlite3.connect('mg.db')

cur = conn.cursor()
cur.execute(sql1)
conn.commit()
conn.close()

# 