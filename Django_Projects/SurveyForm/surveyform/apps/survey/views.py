from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited

def init(request):
    if 'counter' not in request.session:
             request.session['counter'] = 0

def index(request):
    init(request)    
    return render(request,'index.html')

def result(request):
    pass
    return render(request,'result.html')

def process(request): # Perform Data input Processing here...
    if request.method == 'POST':
        request.session['counter'] +=1
        name = request.POST['name']
        loco = request.POST['location']
        fav = request.POST['favLang']
        comm = request.POST['comments']
        email = request.POST['email']

        info = {
            'name': name,
            'loco': loco,
            'fav': fav,
            'comment': comm,
            'email': email
        }
        context = {
            'user': info
        }
    print info
    print 'consider the Page - Processed !!! '
    return render(request,'result.html',context)

def reset(request):
    request.session.flush()
    return redirect('/')