#!/usr/bin/env python

from tinydb import TinyDB, Query

#botar em um config
db = TinyDB('db.json')
userTable = db.table('user')

class UserService():


    def createUser(self):
        
        userTable.insert({'type': 'apple', 'count': 7})
        userTable.insert({'type': 'peach', 'count': 3})