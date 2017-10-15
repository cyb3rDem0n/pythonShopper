import mysql.connector
db = mysql.connector.connect(host='localhost', database='market_basket', user='root', password='toor')
cur = db.cursor()
cur.execute("SELECT * FROM items")

for row in cur.fetchall():
    print row