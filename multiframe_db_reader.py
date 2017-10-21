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
from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["ID", "AMOUNT", "TYPE", "PRICE"]

def get_history():
    # mysql connection, easy man!
    con = db.connector.connect(host='localhost', database='market_basket', user='root', password='toor')
    cur = con.cursor()
    sql = "SELECT * FROM `items`"
    cur.execute(sql)
    lines = cur.fetchall()

    # loop to create for each db tuple a new window containing the relative information
    for val in lines:
        x.add_row(val)
    print x

def get_last():
    print "getLast not ready... Sorry Man"


def insertonclick():
    print "i should insert into DB but..."

def money_spent():
    print "moneySpent not ready... Sorry Man"


def search():
    print "search not ready... Sorry Man"


def show_stats():
    print "showStats not ready... Sorry Man"
