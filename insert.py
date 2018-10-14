import sqlite3

conn = sqlite3.connect('MyDatabase.db')
print("Opened database successfully")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Faruk', 32, 'Sanfrancisco', 120000.00 )")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Hashem', 25, 'Kishorgonj', 115000.00 )")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Monty', 23, 'Narshindi', 120000.00 )")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (5, 'Happy', 25, 'Chittagong ', 165000.00 )")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (6, 'Monty', 23, 'Narshindi', 120000.00 )")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (7, 'Gabriel', 25, 'Khulna ', 165000.00 )")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (8, 'Robert', 23, 'Africa', 120000.00 )")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (9, 'Julia', 25, 'Singapore ', 165000.00 )")

conn.commit()
print("Records created successfully")
conn.close()