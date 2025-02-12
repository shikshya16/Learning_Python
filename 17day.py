#SQLITE DATABASE

import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               email TEXT NOT NULL UNIQUE, 
               password TEXT NOT NULL)
               ''')

#insert multiple data :
users=[
    ('cixya123@gmail.com', 'cixya123'),
    ('shikshya123@gmail.com' , 'shikshya123')
]

#insert single data :
query = '''
    INSERT INTO users(email, password) 
    VALUES
    (?,?)
'''

# cursor.executemany(query, users)


#Retrieving Data :
query = "SELECT * FROM users"
cursor.execute(query)
rows = cursor.fetchall()
print(rows)
# for row in rows:
#     print(row)

#UPDATING DATA : 
# query = "UPDATE users SET password='newpassword' WHERE id = 1"
# cursor.execute(query)

# conn.commit()

cursor.close()
conn.close()

# print(conn)