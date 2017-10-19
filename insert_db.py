from Tkinter import *
import mysql.connector

db = mysql.connector.connect(host='localhost', database='market_basket', user='root', password='toor')
cur = db.cursor()


def insert_db():
    # i need a button action to call in main IF th def
    win_insert = Tk()
    win_insert.title("INSERT WINDOWS")

    # text input box
    Label(win_insert, text="AMOUNT").grid(row=0, column=2)
    amountentry = Entry(win_insert, width=10)
    amountentry.grid(row=1, column=2, sticky=W)

    Label(win_insert, text="TYPE").grid(row=0, column=3)
    typeentry = Entry(win_insert, width=10)
    typeentry.grid(row=1, column=3, sticky=W)

    Label(win_insert, text="PRICE").grid(row=0, column=4)
    priceentry = Entry(win_insert, width=10)
    priceentry.grid(row=1, column=4, sticky=W)

    def to_db():
        amount_ = amountentry.get()
        food_type_ = typeentry.get()
        price_ = priceentry.get()

        print(type(amount_), type(food_type_), type(price_))
        if amount_ != "" and food_type_ != "" and price_ != "":
            ins = "INSERT INTO items (amount,food_type, price) VALUES ( %s, %s, %s)"
            cur.execute(ins, (amount_, food_type_, price_))
            db.commit()
            clear()
        else:
            print "empy"

    def close():
        win_insert.destroy()

    def clear():
        amountentry.delete(0, END)
        typeentry.delete(0, END)
        priceentry.delete(0, END)

    Button(win_insert, text="INSERT", command=to_db, width=12).grid(row=1, column=5)
    Button(win_insert, text="CLOSE", command=close, width=12).grid(row=1, column=6)

    win_insert.mainloop()
