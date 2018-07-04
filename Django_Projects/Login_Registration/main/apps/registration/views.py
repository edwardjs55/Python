# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
import time
from datetime import datetime
from django.utils import timezone
import bcrypt
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import HttpResponse, redirect, render
from .models import User

now = (datetime.now().strftime('%Y-%m-%d'))
# the index function is called when root is visited

def init(request):
    if 'action' not in request.session:
        request.session['action'] = ''
        return

def index(request):
    init(request)
    return render(request, 'registration/index.html')


def register(request):
    if request.method == 'POST':
        post_data = {
            "first_name": request.POST['first_name'],
            "last_name": request.POST['last_name'],
            "email": request.POST['email'],
            # "birthdate": request.POST['birthdate'],
            "password": request.POST['password'],
            "confirm": request.POST['confirm'],
        }
        result = User.objects.register_validator(post_data)
        print result
        print 'result[0]=', result[0]
        if result[0]:  # success
            request.session['user_id'] = result[1]  # result[1].id
            request.session['action'] = 'registered'
            return redirect("/success")
        else:  # failed
            # print '[1]', result[1], result[1]['user_name']
            for item in result[1].values():
                messages.error(request, item, extra_tags='register')

            return redirect("/")
        # request.session['user_id'] = User.objects.get(user_name = user)
        # return redirect('/blogs')
        # return render(request,'travelbuddy/travels.html')


def login(request):
     if request.method == 'POST':
        post_data = {
                "email": request.POST['email'],
                "password": request.POST['password'],
            }
        result = User.objects.login_validator(post_data)

        if result[0]:  # success
            # print result
            request.session['user_id'] = result[1]
            print 'session_id: ', request.session['user_id']
            request.session['action'] = 'Logged In'
            return redirect("/success")
        else:
            # print '[1]', result[1], result[1]['user_name']
            for item in result[1].values():
                messages.error(request, item, extra_tags='login')
            return redirect("/")


def success(request):
    user = User.objects.get(id=request.session['user_id'])
    name = user.first_name
    context = {
        'name': name,
        'action': request.session['action']
    }
    return render(request, 'registration/success.html',context)

def reset(request):    
    request.session.flush()
    return redirect('/')
