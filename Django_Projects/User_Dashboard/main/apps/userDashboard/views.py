# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    return render(request,'userDashboard/index.html')

def signinPage(request): # open the sigin page
    pass
    return

def signin(request): # validate Data
    pass
    return

def registerPage(request): # open Register page
    pass
    return

def register(request): # registration Validation
    pass
    return

def show(request): # Open the Show Page
    pass
    return

def adminDashboard(request): # Open admin Dashboard
    pass
    return

def dashboard(request): # open the userdashboard
    pass
    return

def addUser(request): # Admin User Add Page
    pass
    return

def userEdit(request): # User Profile Edit/self
    pass
    return

def adminEdit(request): # Admin/user edit function
    pass
    return

def userSave(request):
    pass
    return

def adminSave(request):
    pass
    return

