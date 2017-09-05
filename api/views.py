#!/usr/bin/env python
from flask import Flask, request, Response
import services
import models
import json

app = Flask(__name__)
user_service = services.UserService()
usergroup_service = services.UsergroupService()

class HomeController():
   
    @app.route("/")
    def hello():
        return "Welcome to User Manager"

class UserController():
    
    @app.route("/users/<int:user_id>", methods=['GET'])
    def getone_user(user_id):
        return success(user_service.getone(user_id).to_JSON())

    @app.route("/users", methods=['GET'])
    def getall_user():
        return success(models.to_JSON(user_service.getall()))

    @app.route("/users", methods=['POST'])
    def create_user():
        data = request.json
        return success(user_service.create(models.User(
            name=data['name'],
            username=data['username'],
            password=data['password'],
            fk_usergroup=data['fk_usergroup']
        )).to_JSON())

class UsergroupController():
    
    @app.route("/usergroups/<int:usergroup_id>", methods=['GET'])
    def getone_usergroup(usergroup_id):
        return success(usergroup_service.getone(usergroup_id).to_JSON())

    @app.route("/usergroups", methods=['GET'])
    def getall_usergroup():
        return success(models.to_JSON(usergroup_service.getall()))
   
    @app.route("/usergroups", methods=['POST'])
    def create_usergroup():
        return success(usergroup_service.create(models.Usergroup(name=request.json['name'])).to_JSON())


def success(data):
    return Response(data, status=200, mimetype='application/json')