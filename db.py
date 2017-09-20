#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sqlite3
import sys
import os
import logging
import psycopg2

def create_usergroup(cursor):
    logging.info("Criando a tabela usergroup")
    cursor.execute("""
        create table usergroup (
            id integer not null primary key autoincrement,
            name varchar not null
        );
    """)

def create_user(cursor):
    logging.info("Criando a tabela user")
    cursor.execute("""
        create table user (
            id integer not null primary key autoincrement,
            name varchar not null,
            username varchar not null,
            password varchar not null,
            fk_usergroup integer,
            foreign key (fk_usergroup) references usergroup(id)
        );
    """)

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

    dbname = get_db()
    dbtype = os.environ["UM_DATABASE_TYPE"]

    if("sqlite" == dbtype):
        return sqlite3.connect(dbname)
    elif("pg" == dbtype):
        return getpgconn(dbname)
    else:
        logging.error("{0} não existe".format(dbtype))

def get_db():
    return os.environ["UM_DATABASE_NAME"]

def create_all():
    conn = getconn()
    cursor = conn.cursor()
    create_usergroup(cursor)
    create_user(cursor)
    conn.close()
    logging.info("Database [ {0} ] criada com sucesso.".format(get_db()))

def rm_db():
    db = get_db()
    os.remove(db)
    logging.info("Database " + db + " removida com sucesso.")

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    create_all()