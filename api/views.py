#!/usr/bin/env python
from flask import Flask
from api import services
#from api import models

app = Flask(__name__)
userService = services.UserService()

class HomeController():
    
    @app.route("/")
    def hello():
        return "Welcome to User Manager"

class UserController():
    # mudar pra post quando implementar
    @app.route("/createUser",methods=['GET'])
    def createUser():
        userService.createUser()
        return "Success"

