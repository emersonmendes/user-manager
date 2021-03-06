#!/usr/bin/env python

from app import app
import unittest
import os
import db
import json

USERGROUPS_ROUTE = "/usergroups"
USERS_ROUTE = "/users"

class IntegrationTestCase(unittest.TestCase):

    def test_welcome_page(self):
        res = app.test_client(self).get('/')
        self.assertEqual(res.status_code, 200)
        self.assertIsNotNone(res.data)


    # """ Integration tests for Usergroup """

    def create_usergroup(self, name):
        res = app.test_client(self).post(
            USERGROUPS_ROUTE,
            data=json.dumps({ "name": name }),
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 200)
        obj = json.loads(res.data)
        self.assertIsNotNone(obj['id'])
        return obj

    def getone_usergroup(self,id):
        res = app.test_client(self).get(USERGROUPS_ROUTE + "/" + str(id))
        self.assertEqual(res.status_code, 200)
        return json.loads(res.data)

    def test_create_usergroup(self):
        usergroup_name = "Teste Create Usergroup"
        obj = self.create_usergroup(usergroup_name)
        self.assertEqual(obj['name'], usergroup_name)

    def test_update_usergroup(self):
        usergroup_name = "Teste Update Usergroup"
        save_obj = self.create_usergroup(usergroup_name)
        res = app.test_client(self).put(
            USERGROUPS_ROUTE,
            data=json.dumps({ 
                "id" : save_obj['id'],
                "name": usergroup_name + " New"
            }),
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 200)
        update_obj = json.loads(res.data)
        self.assertEqual(update_obj['id'], save_obj['id'])
        self.assertNotEqual(update_obj['name'], usergroup_name)

    def test_getall_usergroup(self):   
        res = app.test_client(self).get(USERGROUPS_ROUTE)
        self.assertEqual(res.status_code, 200)

    def test_getone_usergroup(self): 
        usergroup_name = "Teste GetOne Usergroup"
        save_obj = self.create_usergroup(usergroup_name)
        getone_obj = self.getone_usergroup(save_obj['id'])
        self.assertEqual(getone_obj['name'], usergroup_name)

    def test_getone_usergroup_with_users(self):
        save_user_obj = self.create_user("Teste GetOne Usergroup With Users")
        usergroup_id = save_user_obj['usergroup']['id']
        res = app.test_client(self).get(USERGROUPS_ROUTE + "/" + str(usergroup_id) + USERS_ROUTE)
        self.assertEqual(res.status_code, 200)
        users = json.loads(res.data)['users']
        self.assertIsNotNone(users)
        self.assertIsNone(users[0]['usergroup'])

    def test_delete_usergroup(self): 
        save_obj = self.create_usergroup("Teste Delete Usergroup")
        save_obj_id = save_obj['id']
        self.assertIsNotNone(self.getone_usergroup(save_obj_id))
        res = app.test_client(self).delete(USERGROUPS_ROUTE + "/" + str(save_obj_id))
        self.assertEqual(res.status_code, 200)
        self.assertIsNone(self.getone_usergroup(save_obj_id))


    # """ Integration test for User """

    def create_user(self, name):
        res = app.test_client(self).post(
            USERS_ROUTE,
            data=json.dumps({ 
                "name": name,
                "username": name + "_username",
                "password": name + "_password",
                "usergroup": self.create_usergroup("Teste Create Usergroup For User " + name)
            }),
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 200)
        obj = json.loads(res.data)
        self.assertIsNotNone(obj['id'])
        return obj

    def getone_user(self,id):
        res = app.test_client(self).get(USERS_ROUTE + "/" + str(id))
        self.assertEqual(res.status_code, 200)
        return json.loads(res.data)
    
    def test_create_user(self):
        user_name = "Teste Create User"
        obj = self.create_user(user_name)
        self.assertEqual(obj['name'], user_name)

    def test_update_user(self):
        user_name = "Teste Update User"
        save_obj = self.create_user(user_name)
        res = app.test_client(self).put(
            USERS_ROUTE,
            data=json.dumps({ 
                "id" : save_obj['id'],
                "name": user_name + " New",
                "username": save_obj['username'],
                "password": save_obj['password'],
                "usergroup": save_obj['usergroup']
            }),
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 200)
        update_obj = json.loads(res.data)
        self.assertEqual(update_obj['id'], save_obj['id'])
        self.assertNotEqual(update_obj['name'], user_name)

    def test_getall_user(self):   
        res = app.test_client(self).get(USERS_ROUTE)
        self.assertEqual(res.status_code, 200)

    def test_getone_user(self): 
        user_name = "Teste GetOne user"
        save_obj = self.create_user(user_name)
        getone_obj = self.getone_user(save_obj['id'])
        self.assertEqual(getone_obj['name'], user_name)

    def test_delete_user(self): 
        save_obj = self.create_user("Teste Delete user")
        save_obj_id = save_obj['id']
        self.assertIsNotNone(self.getone_user(save_obj_id))
        res = app.test_client(self).delete(USERS_ROUTE + "/" + str(save_obj_id))
        self.assertEqual(res.status_code, 200)
        self.assertIsNone(self.getone_user(save_obj_id))


if __name__ == '__main__':
    unittest.main()
   