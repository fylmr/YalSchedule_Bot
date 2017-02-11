# -*- coding: utf-8 -*-
# sqlite3 sch.db <  IKBFU_2_KB.sql
import sqlite3
import config


def connect():
    return sqlite3.connect(config.db)


def get_everything(tablename):
    """
    select * from X
    Returns a list of tuples
    """
    con = connect()

    cur = con.cursor()
    cur.execute("select * from " + tablename)
    res = cur.fetchall()

    cur.close()
    return res


def ():
    pass


print get_everything("monday")
