# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# import re
# from django.contrib import messages
from datetime import datetime

import bcrypt,re
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

#import bcrypt # import REGEX libraries
# hash1 = bcrypt.hashpw('test'.encode(), bcrypt.gensalt())
# import md5 # import md5 Hashing
# import os, binascii # import salt stuff

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #email validation string
NAME_REGEX = re.compile(r'^[a-zA-Z]+$') #first name/last name validation string
U_NAME_REGEX = re.compile(r'^[a-zA-Z0-9]+$') #first name/last name validation string
now = (datetime.now().strftime('%Y-%m-%d'))

class UserManager(models.Manager):
    def register_validator(self, postdata):
        errors = {}
        err = False
                 
        if len(postdata['email']) < 3 or (not EMAIL_REGEX.match(postdata['email'])):
            errors["email"] = "Email is INVALID, Try again"
            err = True
        zcount = User.objects.filter(email = postdata['email'] ).count()
        print " email exists/count:",zcount
        if zcount > 0:
            errors["email"] = "That email is in use, Try Logging in"
            return [False,errors]  
        print 'fname: ',postdata['first_name']
        if len(postdata['first_name']) < 3 or (not NAME_REGEX.match(postdata['first_name'])) :
            errors["first_name"] = "First name must be letters and more than 3 characters"        
            err = True
        if len(postdata['last_name']) < 3 or (not NAME_REGEX.match(postdata['last_name'])) :
            errors["last_name"] = "Last name must be letters and more than 3 characters"        
            err = True 
        if len(postdata['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
            err - True
        if (postdata['password']) != postdata['confirm'] or postdata['confirm'] == "" :
            errors["confirm"] = "Password and Confirm must match"
            err = True
        # if (postdata['birthdate'])  == '' or (postdata['birthdate'] > now )  :
        #     errors["birthdate"] = "Invalid Birth date entered"
        #     err = True
        if err:    
            return [False,errors]

        hash1 = bcrypt.hashpw(postdata['password'].encode(), bcrypt.gensalt()) #bcrypt'd Password
        # User.password = hash1
        
        # test, create will save automatically..
        
        new = User.objects.create(first_name = postdata['first_name'], last_name = postdata['last_name'], \
          email=postdata['email'],password=hash1 ) #birthdate = postdata['birthdate'],
        
        # user = User.objects.get(email=postdata['email'])
        user = User.objects.get(email=postdata['email']).id
        return [True,user]


    def login_validator(self, postData): # Validate Login Data
        errors = {}

        err = False
        if len(postData['email']) == 0:
            errors["email"] = " The Email ID cannot be blank"
            err = True
        if len(postData['password']) == 0:
            errors["password"] = " The Password cannot be blank"
            err = True
        if User.objects.filter(email=postData['email']).count() == 0 :        
            errors["email"] = " That Email ID is not listed, try again or Register"
            err = True
        if err:
            return [False,errors]
        else: # Verify Password
            hash1 = User.objects.get(email=postData['email']).password
            if bcrypt.checkpw(postData['password'].encode(), hash1.encode()):
                user = User.objects.get(email=postData['email']).id
                return [True,user] 
            else:
                errors["password"] = " That Password is InValid"
                return [False,errors]
            

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birthdate = models.DateTimeField(auto_now_add = True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
     # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = UserManager()
    # *************************
    def __repr__(self):
        return "<user: {} {} {} {} {}>".format(self.first_name,self.last_name, self.email, self.birthdate, self.id)


class ApptManager(models.Manager): 
     def addApptValidator(self,postData): # Validate New Wish entry                 
         errors = {}
         err = False
         if len(postData['task']) < 3:
            errors["task"] = " The Task cannot be less than 3 characters."
            err = True
         if (postData['date'])  == '' or (postData['date'] < now )  :
            errors["date"] = "Invalid Date entered"
            err = True
         if (postData['time'])  == '' :
            errors["time"] = "Invalid Time entered"
            err = True         
         if err:
            return [False,errors]
            
         else: # save it
             owner = User.objects.get(id=postData['owner']) 
             # print "Date: ", postData['date']
             # print "Time: ", postData['time']
             # sched = datetime.combine(postData['date'],postData['time'])
             # print 'new sched: ',sched
             day = datetime.strptime(postData['date'],'%Y-%m-%d')
             time= datetime.strptime(postData['time'],'%H:%M').time()
             # print '.time = ', time
             # print 'day = ',day
             newday = datetime.combine(day,time)  # create correct Scheduled entry
             # print 'newday: ',newday

             A = Appt.objects.create(task=postData['task'],owner=owner, \
             status=postData['status'],scheduled=newday )

             #user = User.objects.get(email=postData['email']).id
             return [True," "]

     def EditAppt_Validator(self,postData): # Validate New Wish entry
         errors = {}
         err = False
         if len(postData['task']) < 3:
            errors["task"] = " The Task cannot be less than 3 characters."
            err = True
         if (postData['day'])  == '' or (postData['day'] < now )  :
            errors["day"] = "Invalid Date entered"
            err = True
         if (postData['time'])  == '' :
            errors["time"] = "Invalid Time entered"
            err = True         
         if err:
            return [False,errors]

         else: # save it
            # owner = User.objects.get(id=postData['owner'])
            day = datetime.strptime(postData['day'],'%Y-%m-%d')
            time= datetime.strptime(postData['time'],'%H:%M').time()
            newSched = datetime.combine(day,time)
            newStatus = postData['status']
            
            A = Appt.objects.get(id=postData['appt_id'])
            A.task=postData['task']
            A.scheduled=newSched
            A.status=newStatus
            A.save()

            #sced = combined date & time
            # A = Appt.objects.create(task=postData['task'],owner=owner, \
            # status=postData['status'],scheduled=postData['date'])
            # W.items.add(owner)

            #user = User.objects.get(email=postData['email']).id
            return [True," "]     
                        

class Appt(models.Model):
    task = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name = 'task')
    scheduled = models.DateTimeField(auto_now_add = False)
    status = models.CharField(max_length=255)
    # items = models.ManyToManyField(User, related_name='mylist')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
     # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = ApptManager()
    # *************************
    def __repr__(self):
        return "<appt: {} {} {} {} {} >".format(self.task, self.owner,self.status,self.scheduled, self.id)

  

