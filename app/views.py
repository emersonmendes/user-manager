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
    def welcome():
        response = "<style>table, th, td {border: 1px solid black;padding:5px 15px;}</style><table><tr><th>Function</th><th>Route</th><th>Methods</th></tr>"
        for rule in sorted(app.url_map.iter_rules(), key=lambda x: x.rule):
            if (rule.endpoint != 'static'):
                response = response + "<tr><th>" + rule.endpoint + "</th><th>" + rule.rule.replace("<","[").replace(">","]") + "</th><th>" + ','.join(rule.methods) + "</th></tr>"
        return "<h4>Welcome to User Manager :)</h4><br/><br/>Available Resources: <br/><br/>" + response + "</table>"

_users_ep = "/users"
_usergroups_ep = "/usergroups"

class UserController():

    @app.route(_users_ep, methods=['GET'])
    def getall_user():
        return success(to_JSON(user_service.getall()))
    
    @app.route(_users_ep + "/<int:user_id>", methods=['GET'])
    def getone_user(user_id):
        return success(to_JSON(user_service.getone(user_id)))

    @app.route(_users_ep, methods=['POST'])
    def save_user():
        data = request.json
        return success(to_JSON(user_service.save(models.User(
            name=data['name'],
            username=data['username'],
            password=data['password'],
            usergroup=models.Usergroup(id=data["usergroup"]["id"])
        ))))

    @app.route(_users_ep, methods=['PUT'])
    def update_user():
        data = request.json
        return success(to_JSON(user_service.save(models.User(
            data['id'],
            data['name'],
            data['username'],
            data['password'],
            models.Usergroup(id=data['usergroup']['id'])
        ))))

    @app.route(_users_ep + "/<int:user_id>", methods=['DELETE'])
    def delete_user(user_id):
        user_service.delete(user_id)
        return success()


class UsergroupController():

    @app.route(_usergroups_ep, methods=['GET'])
    def getall_usergroup():
        return success(to_JSON(usergroup_service.getall()))
    
    @app.route(_usergroups_ep + "/<int:usergroup_id>", methods=['GET'])
    def getone_usergroup(usergroup_id):
        return success(to_JSON(usergroup_service.getone(usergroup_id)))

    @app.route(_usergroups_ep + "/<int:usergroup_id>/users", methods=['GET'])
    def getone_usergroup_with_users(usergroup_id):
        return success(to_JSON(usergroup_service.getone_with_users(usergroup_id)))
   
    @app.route(_usergroups_ep, methods=['POST'])
    def save_usergroup():
        return success(to_JSON(usergroup_service.save(models.Usergroup(name=request.json['name']))))
    
    @app.route(_usergroups_ep, methods=['PUT'])
    def update_usergroup():
        return success(to_JSON(usergroup_service.save(models.Usergroup(
            request.json['id'],
            request.json['name']
        ))))

    @app.route(_usergroups_ep + "/<int:usergroup_id>", methods=['DELETE'])
    def delete_usergroup(usergroup_id):
        usergroup_service.delete(usergroup_id)
        return success()


def success(data=None):
    return Response(data, status=200, mimetype='application/json')

def to_JSON(obj):
    return json.dumps(obj, sort_keys=True, default=lambda o: o.__dict__) 