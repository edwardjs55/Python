# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from time import gmtime, strftime
import random
def init(request):
    if "gold" not in request.session:
        request.session["gold"] = 0
    if "farm_earn" not in request.session:
        request.session["farm_earn"] = 0    
    if "cave_earn" not in request.session:
        request.session["cave_earn"] = 0    
    if "house_earn" not in request.session:
        request.session["house_earn"] = 0    
    if "casino-earn" not in request.session:
        request.session["casino_earn"] = 0  
    if "logs" not in request.session:
        request.session["logs"] = []
    return True

def index(request):
    init(request)
    context = {
        "time": strftime("%I:%M %p", gmtime()), 
    }
    return render(request, "index.html", context)

def process_money(request):
    if request.method == "POST":
        place = request.POST["building"]
    if place == "farm1":
        winnings = random.randrange(10,21)
        a = "You earned {} gold from the farm!".format(winnings)
        request.session["logs"].append(a)
    if place == "cave1":
        winnings = random.randrange(5,11)
        a = "You earned {} gold from the cave!".format(winnings)
        request.session["logs"].append(a)
    if place == "house1":
        winnings = random.randrange(2,6)
        a = "You earned {} gold from the house!".format(winnings)
        request.session["logs"].append(a)
    if place == "casino1":
        winnings = random.randrange(-50,50)
        a = "You earned {} gold from the casino!".format(winnings)
        request.session["logs"].append(a)
    request.session["gold"] += winnings

    # if winnings < 0:
    #     request.session["logs"].append("You lost!")
    # else:
    #     request.session["logs"].append("You WIN!")
    # print request.session["logs"]

    return redirect("/")
    