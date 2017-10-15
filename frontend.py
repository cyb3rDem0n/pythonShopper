from tkinter import *

# obj window
window=Tk()

l1=Label(window,text="ID ITEMS")
l1.grid(row=0,column=0)

l1=Label(window,text="AMOUNT")
l1.grid(row=0,column=1)

l1=Label(window,text="TYPE")
l1.grid(row=0,column=2)

l1=Label(window,text="PRICE")
l1.grid(row=0,column=3)

#entries
id_text=StringVar()
e1=Entry(window,textvariable=id_text)
e1.grid(row=1,column=0)

#entries
amount_text=StringVar()
e2=Entry(window,textvariable=amount_text)
e2.grid(row=1,column=1)

#entries
type_text=StringVar()
e3=Entry(window,textvariable=type_text)
e3.grid(row=1,column=2)

#entries
price_text=StringVar()
e4=Entry(window,textvariable=price_text)
e4.grid(row=1,column=3)

#button
b1=Button(window,text="Add Entries", width=12)
b1.grid(row=1, column=5)

b2=Button(window,text="Get Values", width=12)
b2.grid(row=1, column=6)

window.mainloop()
