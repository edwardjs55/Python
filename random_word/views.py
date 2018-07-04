# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse,redirect

from django.utils.crypto import get_random_string

def index(request):
    # response = "Time Display Application"
    # return HttpResponse(response)
    if 'counter' not in request.session:
			request.session['counter']=0
    context = {
        "random": get_random_string(length=14)        
        }
    return render(request,'index.html',context)

def generate(request):
    context = {
        "random": get_random_string(length=14)        
        }
    request.session['counter'] += 1
    return render(request,'index.html',context)


def reset(request):
    request.session['counter']=0
    return redirect('/')
# Create your views here.
