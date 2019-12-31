# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.template import RequestContext
import calendar
from LeavePortal.models import Resource,Leave,LeaveType
import datetime
from .forms import LeaveForm
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
    success_message=''
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            obj_count = Leave.objects.filter(leave_date=form.cleaned_data['leave_date'], resource=form.cleaned_data['resource']).count()
            if obj_count == 0:
                # A new leave object created
                form.save()
                success_message = 'Leave added successfully!'
            else:
                # leave object already exists
                leave_obj = Leave.objects.get(leave_date=form.cleaned_data['leave_date'], resource=form.cleaned_data['resource'])
                leave_obj.leave_type = form.cleaned_data['leave_type']
                leave_obj.save()
                success_message = 'Leave updated successfully!'
        else:
            return render(request,'leaves.html',{'form':form})
    form=LeaveForm(initial={'leave_date': 'DD/MM/YYYY'})
    return render(request,'leaves.html',{'form':form,'success_message':success_message})

class Month:
    def __init__(self, name, daycount, number):
        self.name = name
        self.daycount = daycount
        self.number = number

class Resource_leave:
    def __init__(self, full_name, leaves):
        self.full_name = full_name
        self.leaves = leaves
