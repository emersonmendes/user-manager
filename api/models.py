#!/usr/bin/env python

import json

class User():
    
    def __init__(
        self, 
        id=None, 
        name=None, 
        username=None, 
        password=None, 
        fk_usergroup=None
    ):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.fk_usergroup = fk_usergroup

    id = None
    name = None
    username = None
    password = None
    fk_usergroup = None
    
    def to_JSON(self):
        return to_JSON(self)

class Usergroup():

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
    
    id = None
    name = None

    def to_JSON(self):
        return to_JSON(self)


def to_JSON(obj):
    return json.dumps(obj, default=lambda o: o.__dict__) 