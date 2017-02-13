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


def get_day(day):
    """
    select * from Schedule where day = INT
    Returns a tuple of lists
    NOT UNICODE
    """

    con = connect()

    cur = con.cursor()
    cur.execute("select * from Schedule where day = ?", str(day))

    return cur.fetchall()


def get_professor_name(professorId):
    """
    select professorname from Professors where professorId = ?
    Returns a string
    UNICODE
    """

    con = connect()

    cur = con.cursor()
    cur.execute("select professorname from Professors where professorId = ?",
                str(professorId))

    return cur.fetchone()[0]


def get_subject_name(subjectId):
    """
    select name from Subjects where subjectId =
    Returns a string
    UNICODE
    """

    con = connect()

    cur = con.cursor()
    cur.execute("select name from Subjects where subjectId = " +
                str(subjectId))

    return cur.fetchone()[0]


def get_starttime(lessonNumber):
    con = connect()

    cur = con.cursor()
    cur.execute(
        "select starttime from starttimes where lessonnumber = " +
        str(lessonNumber))

    return cur.fetchone()[0]
