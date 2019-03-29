import sqlite3

con = sqlite3.connect("books_db.sqlite3")
cur = con.cursor()   #basic comments to create sql in python(all 3)

try:
	cur.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, 'name INTEGER, rating INTEGER)")
except sqlite3.OperationalError:
	print("Table already exists...")
cur.execute("""INSERT into books VALUES (1, "One Indian Girl", 4)""")
cur.execute("""INSERT into books VALUES (2, "Becoming", 5)""")
cur.execute("""INSERT into books VALUES (3, "Angel's Flight", 5)""")

con.commit()   #to put data to database