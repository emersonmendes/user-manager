#!/usr/bin/env python

import sqlite3

def getconn():
    return sqlite3.connect('user-manager.db')

def getone(query, params):
    conn = getconn()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchone()
    conn.close()
    return result

def getall(query):
    conn = getconn()
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def create(statement, params):
    conn = getconn()
    cursor = conn.cursor()
    cursor.execute(statement, params)
    conn.commit()
    conn.close()
    return cursor.lastrowid