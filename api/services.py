#!/usr/bin/env python

from flask import jsonify
import sqlite3
from api import models

def getconn():
    return sqlite3.connect('user-manager.db')

class UserService():
    
    def create(self,user):
        conn = getconn()
        conn.cursor().execute(
            """ insert into user ( name, username, password, fk_usergroup ) values ( ?, ?, ?, ? ) """,
            (user.name, user.username, user.password, user.fk_usergroup) 
        )
        conn.close()

    def getone(self, id):
        conn = getconn()
        cursor = conn.cursor()
        cursor.execute("select * from user where id = ?",(id))
        result = cursor.fetchone()
        user = models.User()
        user.id = result[0]
        return usergroup
        conn.close()

class UsergroupService():
    
    def create(self, usergroup):
        conn = getconn()
        conn.cursor().execute("insert into usergroup (name) values (?)",(usergroup.name,))
        conn.commit()
        conn.close()
        print result

    def getone(self, id):
        conn = getconn()
        cursor = conn.cursor()
        cursor.execute("select * from usergroup where id = ? ",(id))
        result = cursor.fetchone()
        usergroup = models.Usergroup()
        usergroup.id = result[0]
        usergroup.name = result[1]
        return usergroup
        conn.close()