# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.template import RequestContext
import calendar
from LeavePortal.models import Resource,Leave
import datetime
# Create your views here.

def index(request):
    month_names = ['January','February','March','April','May','June','July','August','September','October','November','December']
    months=[]
    for i in range(1,13):
        months.append(Month(month_names[i-1],range(1,calendar.monthrange(datetime.datetime.now().year,i)[1]+1),str(i)))

    names = list(Resource.objects.all())
    leaves = list(Leave.objects.all())

    resource_leaves = []

    for name in names:
        resource_leaves.append(Resource_leave(name.full_name, [leave for leave in leaves if leave['resource'] == name]))

    return render(request,'index.html',{'months':months, 'names':names, 'leaves':leaves, 'resource_leaves':resource_leaves, 'year':datetime.datetime.now().year})


def leaves(request):
    return render(request,'leaves.html',{'months':months, 'names':names, 'leaves':leaves, 'resource_leaves':resource_leaves})


class Month:
    def __init__(self, name, daycount, number):
        self.name = name
        self.daycount = daycount
        self.number = number

class Resource_leave:
    def __init__(self, full_name, leaves):
        self.full_name = full_name
        self.leaves = leaves
