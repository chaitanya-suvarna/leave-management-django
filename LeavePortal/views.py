# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.template import RequestContext
import calendar
# Create your views here.

def index(request):
    month_names = ['Jan','Feb','Mar','Apr','May','June','Jul','Aug','Sep','Oct','Nov','Dec']
    months=[]
    for i in range(1,13):
        months.append(Month(month_names[i-1],range(1,calendar.monthrange(2019,i)[1]+1)))
    return render(request,'index.html',{'months':months})

class Month:
    def __init__(self, name, daycount):
        self.name = name
        self.daycount = daycount
