from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NewThreadForm
from .models import *
#from .models import * 
def index(request):

    pass

def board(request):
    form = NewThreadForm(request.POST or None)
    if request.method == "POST":
       
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/") #this redirects so you don't resubmit on refresh

    
    posts = Post.objects.order_by('-id')

    
    context = {
        'form':form,
        'posts':posts,
    }
    return render(request, 'boards/main.html', context)

def viewthread(request):


    pass
