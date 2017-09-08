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
                (user.name, user.username, user.usergroup.id, user.id)
            )
        else:
            id = dao.save(
                "insert into user ( name, username, password, fk_usergroup ) values ( ?, ?, ?, ? )",
                (user.name, user.username, user.password, user.usergroup.id)
            )
            user = self.getone(id)
        return user

    def getone(self, id):
        return self.parse(dao.getone("""
            select 
                u.id,
                u.name,
                u.username,
                ug.id,
                ug.name    
            from 
                user u
            join
                usergroup ug on u.fk_usergroup = ug.id
            where u.id = ? 
        """,(id,)))

    def getall(self):
        users = []
        for row in dao.getall("""
            select 
                u.id,
                u.name,
                u.username,
                ug.id
            from 
                user u
            join
                usergroup ug on u.fk_usergroup = ug.id
        """):
            users.append(self.parse(row))
        return users

    def delete(self, id):
        dao.delete("delete from user where id = ?", (id,))

    def parse(self,result):
        if(result is None):
            return None
        return models.User(
            result[0], 
            result[1], 
            result[2], 
            None, 
            models.Usergroup(result[3], result[4])
        )


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
        return self.parse(dao.getone("select * from usergroup where id = ? ",(id,)))

    def getall(self):
        usergroups = []
        for row in dao.getall("select * from usergroup"):
            usergroups.append(self.parse(row))
        return usergroups

    def delete(self, id):
        dao.delete("delete from usergroup where id = ?", (id,))

    def parse(self,result):
        if(result is None):
            return None
        return models.Usergroup(result[0], result[1])