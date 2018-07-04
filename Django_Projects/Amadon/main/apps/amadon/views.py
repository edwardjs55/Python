# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited

def init(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'sale' not in request.session:
        request.session['sale'] = 0
    if 'log' not in request.session:
        request.session['log'] = 0
    return

def index(request):
    init(request)
    return render(request,'amadon/index.html')


def buy(request):
    if request.method == "POST":
        item = request.POST['item']
        qty = int(request.POST['quantity'])
        desc = request.POST['desc']
        # create a dict of item/price
        price = {'1':19.99,'2':29.99,'3': 4.99,'4': 29.99 }
        sale = qty*price[item]
        request.session['sale'] = sale
        request.session['count'] += 1
        request.session['total'] += sale
        log = desc+'  : '+str(qty)+' for  $'+str(sale)        
    
    return redirect('/checkout')

def checkout(request):
    context = {
            'sale': request.session['sale'],
            'items': request.session['count'],
            'total': request.session['total']
        }

    return render(request,'amadon/Checkout.html',context)

def reset(request):
    request.session.flush()
    return redirect('/')