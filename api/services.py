#!/usr/bin/env python

from flask import jsonify
import sqlite3
import models
import dao



class UserService():
    
    def create(self,user):
        id = dao.create(
            "insert into user ( name, username, password, fk_usergroup ) values ( ?, ?, ?, ? )",
            (user.name, user.username, user.password, user.fk_usergroup)
        )
        user.id = id
        return user

    def getone(self, id):
        return self.parse(dao.getone("select * from user where id = ? ",(id,)))

    def getall(self):
        users = []
        for row in dao.getall("select * from user"):
            users.append(self.parse(row))
        return users

    def parse(self,result):
        return models.User(result[0], result[1], result[2], None, result[4])


class UsergroupService():
    
    def create(self, usergroup):
        id = dao.create(
            "insert into usergroup (name) values (?)",
            (usergroup.name,)
        )
        usergroup.id = id
        return usergroup

    def getone(self, id):
        result = dao.getone("select * from usergroup where id = ? ",(id,))
        return self.parse(result)

    def getall(self):
        usergroups = []
        for row in dao.getall("select * from usergroup"):
            usergroups.append(self.parse(row))
        return usergroups

    def parse(self,result):
        return models.Usergroup(result[0], result[1])