#!/usr/bin/env python

import sqlite3
import os

def get_db():
    return os.environ.get('UM_DATABASE')

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
    conn =  sqlite3.connect(db)
    cursor = conn.cursor()
    create_usergroup(cursor)
    create_user(cursor)
    print("Database " + db + " criada com sucesso.")
    conn.close()

def rm_db():
    db = get_db()
    os.remove(db)
    print("Database " + db + " removida com sucesso.")

if __name__ == '__main__':
    create_all()