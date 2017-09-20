#!/usr/bin/env python

import sqlite3
import os
import logging

logging.getLogger().setLevel(logging.INFO)

def getconn():
    return sqlite3.connect(os.environ["UM_DATABASE"])

def getone(query, params):
    conn = getconn()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchone()
    conn.close()
    return result

def getall(query, params=None):
    
    conn = getconn()
    cursor = conn.cursor()
    
    if(params):
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    
    result = cursor.fetchall()
    conn.close()
    
    return result

def save(statement, params):
    conn = getconn()
    cursor = conn.cursor()
    cursor.execute(statement, params)
    conn.commit()
    conn.close()
    return cursor.lastrowid

def delete(model, id):
    conn = getconn()
    cursor = conn.cursor()
    cursor.execute("delete from " + model + " where id = ?", id)
    conn.commit()
    conn.close()