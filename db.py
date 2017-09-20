#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sqlite3
import sys
import os
import logging

def get_db():
    return os.environ["UM_DATABASE"]

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

def create_all():
    db = get_db()
    if(os.path.exists(db)):
        logging.info("Database [ " + db + " ] já existe.")
    else:
        conn =  sqlite3.connect(db)
        cursor = conn.cursor()
        create_usergroup(cursor)
        create_user(cursor)
        conn.close()
        logging.info("Database [ " + db + " ] criada com sucesso.")

def rm_db():
    db = get_db()
    os.remove(db)
    logging.info("Database " + db + " removida com sucesso.")

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    create_all()