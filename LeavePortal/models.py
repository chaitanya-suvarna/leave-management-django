# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Resource(models.Model):
    full_name = models.CharField(max_length=200)

    def __str__(self):
        ret = self.full_name
        return ret

class Leave(models.Model):
    leave_date = models.DateField()
    leave_type = models.IntegerField(default=0)
    resource = models.ForeignKey(Resource,models.CASCADE)

    def __str__(self):
        ret = self.resource.full_name + ', ' + self.leave_date.strftime("%d/%m/%Y") + ', ' + str(self.leave_type)
        return ret

    def __getitem__(self, key):
        return getattr(self, key)
