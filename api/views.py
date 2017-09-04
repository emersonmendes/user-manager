#!/usr/bin/env python
from flask import Flask, request, jsonify
from api import services
from api import models

app = Flask(__name__)
user_service = services.UserService()
usergroup_service = services.UsergroupService()

class HomeController():
   
    @app.route("/")
    def hello():
        return "Welcome to User Manager"

class UserController():
    
    @app.route("/users", methods=['GET'])
    def getone_user():
        return jsonify(user_service.getone(request.args.get('id')))

    @app.route("/users", methods=['POST'])
    def create_user():
       return jsonify(user_service.create(models.User(json = request.json)))

class UsergroupController():
    
    @app.route("/usergroups", methods=['GET'])
    def getone_usergroup():
        return jsonify(usergroup_service.getone(request.args.get('id')).to_JSON())
   
    @app.route("/usergroups", methods=['POST'])
    def create_usergroup():
     return jsonify(usergroup_service.create(models.Usergroup(json = request.json)))