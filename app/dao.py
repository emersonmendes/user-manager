#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import logging

import sqlite3
import psycopg2

logging.getLogger().setLevel(logging.INFO)

def getpgconn(dbname):
    return psycopg2.connect("""
        dbname={0} 
        user={1} 
        host={2}
        password={3}
    """.format(
        dbname,
        os.environ["UM_DATABASE_USER"],
        os.environ["UM_DATABASE_HOST"],
        os.environ["UM_DATABASE_PASS"]
    ))

def getconn():

    dbtype = os.environ["UM_DATABASE_TYPE"]
    dbname = os.environ["UM_DATABASE_NAME"]

    if("sqlite" == dbtype):
        return sqlite3.connect(dbname)
    elif("pg" == dbtype):
        return getpgconn(dbname)
    else:
        logging.error("{0} não existe".format(dbtype))

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