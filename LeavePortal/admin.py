# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from LeavePortal.models import Resource, Leave, LeaveType

# Register your models here.
admin.site.register(Resource)
admin.site.register(Leave)
admin.site.register(LeaveType)
