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
    NOT UNICODE
    """
    con = connect()

    cur = con.cursor()
    cur.execute("select * from " + tablename)
    res = cur.fetchall()
    return res


print get_everything("professors")
