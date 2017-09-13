#!/usr/bin/env python

class User():
    
    def __init__(self,id=None,name=None,username=None,password=None,usergroup=None):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.usergroup = usergroup

    id = None
    name = None
    username = None
    password = None
    usergroup = None


class Usergroup():

    def __init__(self, id=None, name=None, users=None):
        self.id = id
        self.name = name
        self.users = users
    
    id = None
    name = None
    users = None