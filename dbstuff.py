# -*- coding: utf-8 -*-
# sqlite3 sch.db <  IKBFU_2_KB.sql
import sqlite3
import config


def connect():
    con = sqlite3.connect(config.db)
    return con


def get_everything(con):
    cur = con.cursor()
    cur.execute("select * from Monday")
    print cur.fetchall()


get_everything(connect())
