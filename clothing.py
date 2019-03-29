import sqlite3

con = sqlite3.connect("clothing_db.sqlite3")
cur = con.cursor()

try:
	cur.execute("CREATE TABLE clothing (id INTEGER PRIMARY KEY, name TEXT, price INTEGER, quantity INTEGER, availability TEXT)");
except sqlite3.OperationalError:
	print("Table already exists...")

cur.execute("""INSERT INTO clothing VALUES (1, "Shirts", 200, 1, "yes")"""")
cur.execute("""INSERT INTO clothing VALUES (2, "T-shirts", 150, 3, "no")""")
cur.execute("""INSERT INTO clothing VALUES (3, "Trousers", 500, 2, "yes")""")
cur.execute("""INSERT INTO clothing VALUES (4, "Shirts", 200, 1, "yes")""")
cur.execute("""INSERT INTO clothing VALUES (5, "Jeans", 800, 2, "no")""")

con.commit()