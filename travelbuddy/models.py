# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
# from django.contrib import messages
from datetime import datetime

import re, bcrypt
#import bcrypt # import REGEX libraries

# hash1 = bcrypt.hashpw('test'.encode(), bcrypt.gensalt())
# import md5 # import md5 Hashing
# import os, binascii # import salt stuff

#EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #email validation string
NAME_REGEX = re.compile(r'^[a-zA-Z]+$') #first name/last name validation string
U_NAME_REGEX = re.compile(r'^[a-zA-Z0-9]+$') #first name/last name validation string

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        name = postData['name']
        user = postData['user_name']
        password = postData['password']
        confirm = postData['confirm']

        # check for duplicate user_name
        # print 'user: ',user
        err = False
        
        zcount = User.objects.filter(user_name = user).count()
        print " user exists/count:",zcount
        if zcount > 0:
            errors["user_name"] = "That user name is in use, pick another"
            return [False,errors]
        if len(user) < 2 or (not U_NAME_REGEX.match(user)):
            errors["user_name"] = "User name must be more than 2 characters"
            err = True        
        if len(name) < 2 or (not NAME_REGEX.match(name)) :
            errors["name"] = "Name must be letters and more than 2 characters"        
            err = True        
        if len(password) < 8:
            errors["password"] = "Password should be at least 8 characters"
            err - True
        if (password) != confirm or confirm == "" :
            errors["confirm"] = "Password and Confirm must match"
            err = True
        if err:    
            return [False,errors]

        hash1 = bcrypt.hashpw(password.encode(), bcrypt.gensalt()) #bcrypt'd Password
        # User.password = hash1
        new = User.objects.create(name = name,user_name=user,password=hash1 )
        new.save()
        return [True,new]


    def login_validator(self, postData): # Validate Login Data
        errors = {}
        user = postData['user_name']
        password = postData['password']

        err = False
        if len(user) == 0:
            errors["user_name"] = " The User logon cannot be blank"
            # print errors['user_name']
            err = True
        if len(password) == 0:
            errors["password"] = " The Password cannot be blank"
            err = True
        if User.objects.filter(user_name=user).count() == 0 :        
            errors["password"] = " That User Name is not listed, try again or Register"
            err = True
        if err:
            return [False,errors]
        else: # Verify Password
            hash1 = User.objects.get(user_name=user).password
            if bcrypt.checkpw(password.encode(), hash1.encode()):
                user = User.objects.get(user_name=user).id
                return [True,user] 
            else:
                errors["password"] = " That Password is InValid"
                return [False,errors]
            

class User(models.Model):
    name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
     # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = UserManager()
    # *************************
    def __repr__(self):
        return "<user: {} {} {}>".format(self.name, self.user_name, self.id)


class TripManager(models.Manager): 
     def addTrip_validator(self,postData): # Validate New Trip entry
        errors = {} 
        # user_id = request.Session['user_id']  

        # Validation Table
        now = (datetime.now().strftime('%Y-%m-%d'))
        print postData
        print 'Now: ',now,'  start:', postData['travelstart']
        print "Greater ?: ",  postData['travelstart'] > now
        # print "Tstart", postData['travelstart']
        # print "is it blank ??", postData['travelstart'] == ''
        err = False
        if len(postData['description'] ) < 1:
            errors['description'] = "Description cannot be blank"
            err = True
        if len(postData['destination']) < 1:
            errors['destination'] = 'Destination cannot be blank'
            err = True
        if postData['travelstart'] == '':
            errors['travelstart'] = 'Travel Start Date cannot be blank'
            err = True
        if postData['travelend'] == '':
            errors['travelend'] = 'Travel End Date cannot be blank'
            err = True
        if postData['travelstart'] < now:
            errors['travelstart'] = 'Travel Start date must be a future date'
            err = True
        if postData['travelstart'] > postData['travelend']:
            errors['travelend'] = 'Travel End Date must be after Travel Start Date'
            err = True 

        if errors:
            return [False,errors]
        else:
            try: # Save Data & add to users list                
                T = Trip.objects.create(description = postData['description'], \
                destination = postData['destination'], travel_start = postData['travelstart'], \
                travel_end = postData['travelend'], planner= User.objects.get(id=postData['user_id']))
                usertrips = User.objects.get(id=1).trips.all()
                traveler = User.objects.get(id=postData['user_id'])
                T.travelers.add(traveler)
                
                return [True,usertrips]
                
            except ObjectDoesNotExist:
                errors['notsaved'] = 'could not save Data ??'
                return [False,errors]          
   

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    travel_start = models.DateTimeField(auto_now_add = True)
    travel_end = models.DateTimeField(auto_now_add = True)
    planner = models.ForeignKey(User, related_name = 'plans')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    travelers = models.ManyToManyField(User, related_name= 'trips')
    
     # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = TripManager()
    # *************************
    def __repr__(self):
        return "<trip: {} {} {}>".format(self.destination, self.description, self.id)






