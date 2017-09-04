#!/usr/bin/env python

import json

class User():
    
    id = None
    name = None
    username = None
    password = None
    fk_usergroup = None

    def __init__(self, json = None):
        if(json is not None):
            self.id = json['id']
            self.name = json['name']
            self.username = json['username']
            self.password = json['password']
            self.fk_usergroup = json['fk_usergroup']
    
    def to_JSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__)) 

class Usergroup():
    
    id = None
    name = None

    def __init__(self, json = None):
        if(json is not None):
            self.id = json['id']
            self.name = json['name']
    
    def to_JSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__)) 