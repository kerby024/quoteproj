# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..logreg_app.models import User
from django.db import models

class QuoteManager(models.Manager):
    def quote_validation(self,data):
        errors = {}
        if len(data['author']) < 4:
            errors["author"] = "Author's name needs to be at least 4 characters"

        if len(data['message']) < 10:
            errors["message"] = "Message needs to be at least 10 characters"
    
        return errors

    def addfavorites(self, userid, quoteid):
        f1 = User.objects.get(id = userid)
        f2 = Quote.objects.get(id = quoteid)
        f2.favorites.add(f1)
        f2.save()

    def removefavorites(self, userid, quoteid):
        f1 = User.objects.get(id = userid)
        f2 = Quote.objects.get(id = quoteid)
        f2.favorites.remove(f1)
        f2.save()

class Quote(models.Model):
    user = models.ForeignKey(User, related_name='people')
    author = models.CharField(max_length = 255)
    message = models.TextField(max_length = 1000)
    favorites = models.ManyToManyField(User, related_name='faves')
    objects = QuoteManager()
# Create your models here.
