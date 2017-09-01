#!/usr/bin/env python

from tinydb import TinyDB, Query
from flask import jsonify

#botar em um config
db = TinyDB('db.json')

class UserService():
    
    userTable = db.table('user')
    User = Query()
    
    def createUser(self,user):
        return self.userTable.insert(user.to_JSON())

    def get(self, eid):
        return self.userTable.get(eid = eid)