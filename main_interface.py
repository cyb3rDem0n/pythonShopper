__author__ = "Giuseppe D'Agostino"
__copyright__ = "Copyright 2017, The Fucking Project"
__credits__ = ["Giovanni Peda', Pasquale Labate"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Giuseppe D'Agostino"
__email__ = "dagostinogiuseppe@outlook.com"
__status__ = "Production"

from Tkinter import *
from multiframe_db_reader import *

# exit button
def close_window():
    gui.destroy()
    exit()


gui = Tk()
gui.title("Shopping Memories")
gui.resizable(width=False, height=False)


Label(gui, text="This Is Not A Porno Shop").grid(row=0, column=1)

Button(gui, text="HISTORY", width=12, command=get_history).grid(row=1, column=0)
Button(gui, text="INSERT", width=12, command=insert_new()).grid(row=1, column=2)
Button(gui, text="GET LAST", width=12, command=get_last()).grid(row=2, column=0)
Button(gui, text="MONEY SPENT", width=12, command=money_spent()).grid(row=2, column=2)
Button(gui, text="SEARCH", width=12 ,command=search()).grid(row=3, column=0)
Button(gui, text="SHOW STATS", width=12, command=show_stats()).grid(row=3, column=2)

Button(gui, text="EXIT", width=12 ,command=close_window).grid(row=4, column=1)

gui.mainloop()
