#!/usr/bin/env python

from flask import jsonify
import sqlite3
import models
import dao


class UserService():
    
    def save(self,user):
        if(user.id):
            dao.save(
                "update user set name = ?, username = ?, fk_usergroup = ? where id = ?",
                (user.name, user.username, user.fk_usergroup, user.id)
            )
        else:
            id = dao.save(
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

    def delete(self, id):
        dao.delete("delete from user where id = ?", (id,))

    def parse(self,result):
        return models.User(result[0], result[1], result[2], None, result[4])


class UsergroupService():
    
    def save(self, usergroup):
        if(usergroup.id):
            dao.save(
                "update usergroup set name = ? where id = ?",
                (usergroup.name, usergroup.id)
            )
        else:
            id = dao.save(
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

    def delete(self, id):
        dao.delete("delete from usergroup where id = ?", (id,))

    def parse(self,result):
        return models.Usergroup(result[0], result[1])