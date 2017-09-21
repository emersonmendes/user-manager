#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import logging
import psycopg2

logging.getLogger().setLevel(logging.INFO)

def getconn():
    return psycopg2.connect("""
        dbname={0} 
        user={1} 
        host={2}
        password={3}
    """.format(
        os.environ["UM_DATABASE_NAME"],
        os.environ["UM_DATABASE_USER"],
        os.environ["UM_DATABASE_HOST"],
        os.environ["UM_DATABASE_PASS"]
    ))

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
    cursor.execute(statement + " returning id", params)
    conn.commit()
    id = cursor.fetchone()[0]
    conn.close()
    return id

def delete(model, id):
    conn = getconn()
    cursor = conn.cursor()
    cursor.execute("delete from " + model + " where id = %s", id)
    conn.commit()
    conn.close()