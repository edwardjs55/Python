# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import User,Trip
from django.contrib import messages
import bcrypt


# the index function is called when root is visited

def index(request):
    if 'user_id' not in request.session:
        request.session['user_id'] = -1    
    return render(request,'travelbuddy/index.html')

def register(request):
    result = User.objects.register_validator(request.POST)
    print result
    print 'result[0]=', result[0]
    if result[0]:
        request.session['user_id'] = result[1].id
        return redirect("/travels")
    else:
        # print '[1]', result[1], result[1]['user_name']
        for item in result[1].values():
            messages.error(request, item)
        
        return redirect("/")   
    
      
        request.session['user_id'] = User.objects.get(user_name = user)
        #return redirect('/blogs')
        return render(request,'travelbuddy/travels.html')

def login(request):
    result = User.objects.login_validator(request.POST)

    if result[0]:
        print result
        request.session['user_id'] = result[1]
        return redirect("/travels")
    else:
        # print '[1]', result[1], result[1]['user_name']
        for item in result[1].values():
            messages.error(request, item)
        
        return redirect("/")     

def travels(request):   # show users Travel Plans & other Users travel plans W joim option
    # get travel plans for User
    # get travel plans for Others

        u_id = request.session['user_id']
        user = User.objects.get(id=u_id)
        user_n = user.user_name
        travels = User.objects.get(id=u_id).trips.all()  #get returns an OBJECT
        # others = User.objects.exclude(id=u_id).trips.all() # exclude returns a Qset
        others = Trip.objects.exclude(travelers__id = u_id) #.values('travelers__name', \
        # 'destination','travel_start','travel_end','id')
        context = {
            'user': user_n,
            'trips': travels, 
            'others': others
        }
        return render(request,'travelbuddy/travels.html',context)

def join(request,trip_id): # Add User to trip and display trip details via destination page
    print'TRIP: ', trip_id

    T= Trip.objects.get(id=trip_id)
    T.travelers.add(request.session['user_id'])

    return redirect('/travels')

def destination(request,trip_id):  # details about One Trip & who;s going
    # trip = trip.objects.get( trip_id= trip)
    info = Trip.objects.get(id=trip_id)
    print ' destination info:', info, info.planner.name
    #  planner = info.planner
    # print 'planner=',planner
    #   name = User.objects.get(id=planner).name
    # print 'NAME: ',name
    # print info
    # print info.destination    
    context = {
        #"name": name,
        "tripinfo": info,
        "othernames": info.travelers.all(),
    }
    
    return render(request,'travelbuddy/destination.html',context)

def addplan(request):
    # Button from Travel page to go to the addtrip page to enter trip data
    return render(request,'travelbuddy/addtrip.html')


def createtrip(request): # Verify data & add the trip n go to Travels page    
    postdata = {
                "destination": request.POST['destination'],
                "description": request.POST['description'],
                "travelstart": request.POST['travelstart'],
                "travelend": request.POST['travelend'],
                "user_id": request.session['user_id'],
        }
    result = Trip.objects.addTrip_validator(postdata)

    if result[0]:
        print result[1]
        return redirect('/travels')
    else:
        # print '[1]', result[1], result[1]['user_name']
        print result
        for item in result[1].values():
            messages.error(request, item)
        return render(request,'travelbuddy/addtrip.html')

def logout(request): # delete user cookie N goto root page
    request.session.clear()
    return redirect('/')    

 






