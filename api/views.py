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

    @app.route("/users", methods=['GET'])
    def getall_user():
        return success(to_JSON(user_service.getall()))
    
    @app.route("/users/<int:user_id>", methods=['GET'])
    def getone_user(user_id):
        return success(to_JSON(user_service.getone(user_id)))

    @app.route("/users", methods=['POST'])
    def save_user():
        data = request.json
        return success(to_JSON(user_service.save(models.User(
            name=data['name'],
            username=data['username'],
            password=data['password'],
            usergroup=models.Usergroup(id=data["usergroup"]["id"])
        ))))

    @app.route("/users", methods=['PUT'])
    def update_user():
        data = request.json
        return success(to_JSON(user_service.save(models.User(
            data['id'],
            data['name'],
            data['username'],
            data['fk_usergroup']
        ))))

    @app.route("/users/<int:user_id>", methods=['DELETE'])
    def delete_user(user_id):
        user_service.delete(user_id)
        return success()

class UsergroupController():

    @app.route("/usergroups", methods=['GET'])
    def getall_usergroup():
        return success(to_JSON(usergroup_service.getall()))
    
    @app.route("/usergroups/<int:usergroup_id>", methods=['GET'])
    def getone_usergroup(usergroup_id):
        return success(to_JSON(usergroup_service.getone(usergroup_id)))
   
    @app.route("/usergroups", methods=['POST'])
    def save_usergroup():
        return success(to_JSON(usergroup_service.save(models.Usergroup(name=request.json['name']))))
    
    @app.route("/usergroups", methods=['PUT'])
    def update_usergroup():
        return success(to_JSON(usergroup_service.save(models.Usergroup(
            request.json['id'],
            request.json['name']
        ))))

    @app.route("/usergroups/<int:usergroup_id>", methods=['DELETE'])
    def delete_usergroup(usergroup_id):
        usergroup_service.delete(usergroup_id)
        return success()


def success(data=None):
    return Response(data, status=200, mimetype='application/json')

def to_JSON(obj):
    return json.dumps(obj, default=lambda o: o.__dict__) 