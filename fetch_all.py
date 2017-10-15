import mysql as db
import mysql.connector
from tkinter import *

# data will displayed in a single text box, bad way, i'll try a multiwindows reader, one window for each tuple

con = db.connector.connect(host='localhost', database='market_basket', user='root', password='toor')
cur = con.cursor();

# CREATE A WINDOW
window = Tk()
window.title("FETCH DB DATA")

# CREATE n TEXT BOX TO SHOW ITEMS VALUES AND A LABEL 4 EACH ONE

Label(window, text="ID: ").grid(row=0, column=0)
output_id = Text(window, width=6, height=1, wrap=WORD)
output_id.grid(row=0, column=1, sticky=W)

Label(window, text="AMOUNT: ").grid(row=1, column=0)
output_amount = Text(window, width=6, height=1, wrap=WORD)
output_amount.grid(row=1, column=1, sticky=W)

Label(window, text="TYPE: ").grid(row=2, column=0)
output_type = Text(window, width=10, height=1, wrap=WORD)
output_type.grid(row=2, column=1, sticky=W)

Label(window, text="PRICE: ").grid(row=3, column=0)
output_price = Text(window, width=6, height=1, wrap=WORD)
output_price.grid(row=3, column=1, sticky=W)


# FETCH ALL DATA AND FILL THE TEXT BOX ON CLICK
def click():
    try:
        sql = "SELECT * FROM `items`"
        cur.execute(sql)
    except:
        print "ERROR"
    items = cur.fetchall()
    for val in items:
        output_id.insert(INSERT, val[0])
        output_amount.insert(INSERT, val[1])
        output_type.insert(INSERT, val[2])
        output_price.insert(INSERT, val[3])

Button(window, text = "FETCH", command = click) .grid(row = 5, column = 0)

window.mainloop()
