__author__ = "Giuseppe D'Agostino"
__copyright__ = "Copyright 2017, The Fucking Project"
__credits__ = ["Giovanni Peda', Pasquale Labate"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Giuseppe D'Agostino"
__email__ = "dagostinogiuseppe@outlook.com"
__status__ = "Production"

import mysql as db
import mysql.connector
from tkinter import *


def get_history():
    # mysql connection, easy man!
    global window
    con = db.connector.connect(host='localhost', database='market_basket', user='root', password='toor')
    cur = con.cursor()
    sql = "SELECT * FROM `items`"
    cur.execute(sql)
    rez = cur.fetchall()

    # loop to create for each db tuple a new window containing the relative information
    for val in rez:
        # funny games with window of Tkinter
        window = Tk()
        window.title("Basket Shop")
        window.resizable(width=False, height=False)
        # window.geometry('{}x{}'.format(250, 130))

        # Column of a Basket Shop record
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

        # its time to fill the precedent text box
        output_id.insert(INSERT, val[0])
        output_amount.insert(INSERT, val[1])
        output_type.insert(INSERT, val[2])
        output_price.insert(INSERT, val[3])

    window.mainloop()


def get_last():
    print "getLast not ready... Sorry Man"


def insertonclick():
    print "i should insert into DB but..."


# or i make a new file for each CRUD method with his
# own button, or i show on the main IF, a insert form,
# and a button to insert on db...


def money_spent():
    print "moneySpent not ready... Sorry Man"


def search():
    print "search not ready... Sorry Man"


def show_stats():
    print "showStats not ready... Sorry Man"
