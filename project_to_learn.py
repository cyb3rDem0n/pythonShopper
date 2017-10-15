from tkinter import *


# key down function
def click():
    entered_value = textentry.get()
    output.delete(0.0, END)  # clean
    try:
        my_type = my_list[entered_value]
    except:
        my_type = "not a valid value"
    output.insert(END, my_type)


# main
window = Tk()
window.title("Python Market Basket")

# button
Button(window, text="FETCH", command=click).grid(row=0, column=3, sticky=W)

Label(window, text="Response").grid(row=2, column=0)

# text box
output = Text(window, width=20, height=1, wrap=WORD)
output.grid(row=2, column=1, sticky=W)

Label(window, text="Insert Value Here").grid(row=0, column=0)

# text input box
textentry = Entry(window, width=10)
textentry.grid(row=0, column=1, sticky=W)


# exit button
def close_window():
    window.destroy()
    exit()


# exit button
Button(window, text="EXIT", command=close_window).grid(row=2, column=3, sticky=W)

# dictionary
my_list = {'A': 'Type A selected', 'B': 'Type B selected'}

window.mainloop()
