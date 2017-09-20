#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import logging
import psycopg2

def create_sequence(cursor,seq):
    logging.info("Criando a sequencia {0}".format(seq))
    cursor.execute("create sequence {0} start 1".format(seq))

def create_usergroup(cursor):
    logging.info("Criando a tabela usergroup")
    cursor.execute("""
        create table usergroup (
            id bigint not null,
            name varchar not null
            constraint pk_usergroup primary key (id)
        );
    """)

def create_user(cursor):
    logging.info("Criando a tabela user")
    cursor.execute("""
        create table user (
            id bigint not null,
            name varchar not null,
            username varchar not null,
            password varchar not null,
            fk_usergroup integer,
            constraint pk_user primary key (id)
            constraint fk_usergroup foreign key (fk_usergroup) references usergroup(id)
        );
    """)

def get_db():
    return os.environ["UM_DATABASE_NAME"]

def getconn():
    return psycopg2.connect("""
        dbname={0} 
        user={1} 
        host={2}
        password={3}
    """.format(
        get_db(),
        os.environ["UM_DATABASE_USER"],
        os.environ["UM_DATABASE_HOST"],
        os.environ["UM_DATABASE_PASS"]
    ))

def create_all():
    conn = getconn()
    cursor = conn.cursor()
    create_usergroup(cursor)
    create_user(cursor)
    create_sequence(cursor,"usergroup_seq")
    create_sequence(cursor,"user_seq")
    conn.close()
    logging.info("Database [ {0} ] criada com sucesso.".format(get_db()))

def rm_db():
    db = get_db()
    os.remove(db)
    logging.info("Database " + db + " removida com sucesso.")

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    create_all()