# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.template import RequestContext
# Create your views here.

def index(request):
    return render(request,'index.html',{})
