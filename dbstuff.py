# -*- coding: utf-8 -*-

import sqlite3
import config

def connect():
    con = sqlite3.connect(config.db)
    return con 

def get_everything(con):
    """
    
    """
    cur = con.cursor()
    cur.execute("select * from IKBFU_2_KB")
    print cur.fetchall()

get_everything(connect())