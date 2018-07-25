# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def registration_validation(self, data):
        errors = {}
        if len(data['name']) < 2:
            errors["name"] = "Name needs to be at least 2 characters"

        if len(data['alias']) < 2:
            errors["alias"] = "Alias needs to be at least 2 characters"

        if len(data['password']) < 8:
            errors["password"] = "Password needs to be at least 8 characters"
        
        if not data['password'] == data['confirm']:
            errors["password"] = "Passwords do not match"
        return errors

    def user_validation(self,data):
        errors = {}
        
        existing_user = User.objects.filter(email_address = data['email'])

        if len(existing_user) < 1:
            errors["email"] = "Email does not match our records"

        else:
            print existing_user
            print existing_user[0]
            print existing_user[0].password
            if data['password'] != existing_user[0].password:
                errors["password"] = "Password does not match our records for that email"
        return errors

class User(models.Model):
    name= models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email_address = models.CharField(max_length = 255, unique = True)
    password = models.CharField(max_length = 255)
    dob = models.DateField(auto_now=False)
    objects = UserManager()

 

# Create your models here.
