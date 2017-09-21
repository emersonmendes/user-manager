#!/usr/bin/env python
import json
from . import services, models

from flask import Flask, request, Response, render_template

app = Flask(__name__)
user_service = services.UserService()
usergroup_service = services.UsergroupService()

USERS_ROUTE = "/users"
USERGROUPS_ROUTE = "/usergroups"

class HomeController():

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.route("/")
    def welcome():
        rules = []
        for rule in sorted(app.url_map.iter_rules(), key=lambda x: x.rule):
            if (rule.endpoint != 'static'):
                rules.append({
                    "function" : rule.endpoint,
                    "route" : rule.rule,
                    "method" : ','.join(rule.methods)
                }) 
        return render_template('home.html',rules=rules)

class UserController():

    @app.route(USERS_ROUTE, methods=['GET'])
    def getall_user():
        return success(to_JSON(user_service.getall()))
    
    @app.route(USERS_ROUTE + "/<int:user_id>", methods=['GET'])
    def getone_user(user_id):
        return success(to_JSON(user_service.getone(user_id)))

    @app.route(USERS_ROUTE, methods=['POST'])
    def save_user():
        data = request.json
        return success(to_JSON(user_service.save(models.User(
            name=data['name'],
            username=data['username'],
            password=data['password'],
            usergroup=models.Usergroup(id=data["usergroup"]["id"])
        ))))

    @app.route(USERS_ROUTE, methods=['PUT'])
    def update_user():
        data = request.json
        return success(to_JSON(user_service.save(models.User(
            data['id'],
            data['name'],
            data['username'],
            data['password'],
            models.Usergroup(id=data['usergroup']['id'])
        ))))

    @app.route(USERS_ROUTE + "/<int:user_id>", methods=['DELETE'])
    def delete_user(user_id):
        user_service.delete(user_id)
        return success()


class UsergroupController():

    @app.route(USERGROUPS_ROUTE, methods=['GET'])
    def getall_usergroup():
        return success(to_JSON(usergroup_service.getall()))
    
    @app.route(USERGROUPS_ROUTE + "/<int:usergroup_id>", methods=['GET'])
    def getone_usergroup(usergroup_id):
        return success(to_JSON(usergroup_service.getone(usergroup_id)))

    @app.route(USERGROUPS_ROUTE + "/<int:usergroup_id>" + USERS_ROUTE, methods=['GET'])
    def getone_usergroup_with_users(usergroup_id):
        return success(to_JSON(usergroup_service.getone_with_users(usergroup_id)))
   
    @app.route(USERGROUPS_ROUTE, methods=['POST'])
    def save_usergroup():
        return success(to_JSON(usergroup_service.save(models.Usergroup(name=request.json['name']))))
    
    @app.route(USERGROUPS_ROUTE, methods=['PUT'])
    def update_usergroup():
        return success(to_JSON(usergroup_service.save(models.Usergroup(
            request.json['id'],
            request.json['name']
        ))))

    @app.route(USERGROUPS_ROUTE + "/<int:usergroup_id>", methods=['DELETE'])
    def delete_usergroup(usergroup_id):
        usergroup_service.delete(usergroup_id)
        return success()


def success(data=None):
    return Response(data, status=200, mimetype='application/json')

def to_JSON(obj):
    return json.dumps(obj, sort_keys=True, default=lambda o: o.__dict__) 