#!/usr/bin/env python

import json

class User():
  
    name = None
    username = None
    password = None

    def __init__(self, json):
        self.name = json['name']
        self.username = json['username']
        self.password = json['password']
    
    def to_JSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__)) 
    
    # estudar pra ver como funciona json e None


