#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sqlite3
import sys
import os

db_name="user-manager.db"

def get_db():
    args = sys.argv
    for i, arg in enumerate(args):
        if(arg == "--database"):
            db_name = args[i + 1]
    return db_name

def create_usergroup(cursor):
    cursor.execute("""
        create table usergroup (
            id integer not null primary key autoincrement,
            name varchar not null
        );
    """)

def create_user(cursor):
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
        print("Database [ " + db + " ] já existe.")
    else:
        conn =  sqlite3.connect(db)
        cursor = conn.cursor()
        create_usergroup(cursor)
        create_user(cursor)
        conn.close()
        print("Database [ " + db + " ] criada com sucesso.")

def rm_db():
    db = get_db()
    os.remove(db)
    print("Database " + db + " removida com sucesso.")

if __name__ == '__main__':
    create_all()