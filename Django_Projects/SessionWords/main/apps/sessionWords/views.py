# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
from datetime import datetime
# now = (datetime.now().strftime('%I:%M %p  %Y-%m-%d'))

def init(request):
    if 'wordlist' not in request.session:
        request.session['wordlist'] = []
            
    return

def index(request):
    init(request)
    return render(request,'index.html')

def addWord(request): # get input: word,color & big values
     now = (datetime.now().strftime('%I:%M %p  %Y-%m-%d'))    
     if request.method == 'POST':
         word = request.POST['word']
         color = request.POST['color']
         if 'size' in request.POST:
             size = request.POST['size']
             size='big'
         else:
             size = ''
         if 'wordlist' not in request.session:
             request.session['wordlist'] = []        
         words = [{
             'word': word,
             'color': color,
             'size': size,
             'time': now,
         }]
         request.session['wordlist'] += words
         # print request.session['wordlist']
        #  request.session['wordlist'].append({
        #      'word': word,
        #      'color': color,
        #      'size': size,
        #      'time': now,
        #      })   
         context = {
             'words':request.session['wordlist']
         }
         return render(request,'index.html',context)

def clear(request):        
    request.session.flush()   # request.session.clear()
    print 'Clear button pressed'
    return redirect('/')

