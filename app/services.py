#!/usr/bin/env python

from . import models, dao

class UserService():
    
    def save(self,user):
        if(user.id):
            dao.save(
                "update \"user\" set name = %s, username = %s, password = %s, fk_usergroup = %s where id = %s",
                (user.name, user.username, user.password, user.usergroup.id, user.id)
            )
        else:
            id = dao.save(
                "insert into \"user\" ( id, name, username, password, fk_usergroup ) values ( nextval('user_seq'), %s, %s, %s, %s )",
                (user.name, user.username, user.password, user.usergroup.id)
            )
            user = self.getone(id)
        return user

    def getone(self, id):
        return self.parse(dao.getone("""
            select 
                u.id, u.name, u.username, u.password, ug.id, null   
            from 
                \"user\" u
            join
                usergroup ug on u.fk_usergroup = ug.id
            where u.id = %s
        """,(id,)))

    def getall(self):
        users = []
        for row in dao.getall("""
            select 
                u.id, u.name, u.username, u.password, ug.id, null
            from 
                \"user\" u
            join
                usergroup ug on u.fk_usergroup = ug.id
        """):
            users.append(self.parse(row))
        return users

    def get_by_usergroup(self, fk_usergroup):
        users = []
        for row in dao.getall("""
            select 
                u.id, u.name, u.username, u.password, ug.id, null
            from 
                \"user\" u
            join
                usergroup ug on u.fk_usergroup = ug.id
            where
                u.fk_usergroup = %s
        """, (fk_usergroup,)):
            users.append(self.parse(row,includes_usergroup=False))
        return users

    def delete(self, id):
        dao.delete("\"user\"", (id,))

    def parse(self,r,includes_usergroup=True):
        
        if(r is None):
            return None
        
        if(includes_usergroup):
            usergroup=models.Usergroup(r[4],r[5])
        else:
            usergroup=None

        return models.User(r[0],r[1],r[2],r[3], usergroup)


userService = UserService()

class UsergroupService():
    
    def save(self, usergroup):
        if(usergroup.id):
            dao.save(
                "update usergroup set name = %s where id = %s",
                (usergroup.name, usergroup.id)
            )
        else:
            id = dao.save(
                "insert into usergroup (id, name) values (nextval('usergroup_seq'), %s)", 
                (usergroup.name,)
            )
            usergroup.id = id
        return usergroup

    def getone(self, id):
        return self.parse(dao.getone("select id, name from usergroup where id = %s ",(id,)))

    def getone_with_users(self, id):
        usergroup = self.getone(id)
        usergroup.users = userService.get_by_usergroup(id)
        return usergroup

    def getall(self):
        usergroups = []
        for row in dao.getall("select id, name from usergroup"):
            usergroups.append(self.parse(row))
        return usergroups

    def delete(self, id):
        dao.delete("usergroup", (id,))

    def parse(self,r):
        if(r is None):
            return None
        return models.Usergroup(r[0],r[1])