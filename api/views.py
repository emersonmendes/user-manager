#!/usr/bin/env python
from flask import Flask, request, jsonify
from api import services
from api import models

app = Flask(__name__)
userService = services.UserService()

class HomeController():
   
    @app.route("/")
    def hello():
        return "Welcome to User Manager"

class UserController():
    
    @app.route("/users", methods=['POST'])
    def createUser():
        user = models.User(json = request.json);
        print(userService.createUser(models.User(json = request.json)))
        return "\nSuccess VERIFICAR DE VOLTAR O JSON\n\n"

    @app.route("/users", methods=['GET'])
    def getUserById():
        userService.get(request.args.get('eid'))
        return "\nSuccess VERIFICAR DE VOLTAR O JSON\n\n" 
