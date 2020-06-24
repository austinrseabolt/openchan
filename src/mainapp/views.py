from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NewThreadForm
from .models import *
#from .models import * 
def index(request):
    return HttpResponse("OpenChan")


def board(request, boardurl):
    form = NewThreadForm(request.POST or None)
    currentboard = Board.objects.get(board_url=boardurl)
    if request.method == "POST":
       
        if form.is_valid():
            newpost = form.save(commit=False)
            currentboard.post_counter += 1
            newpost.parent_board = currentboard
            newpost.local_id = currentboard.post_counter
            newpost.save()
            currentboard.save()
            return HttpResponseRedirect("/" + str(currentboard.board_url)) #this redirects so you don't resubmit on refresh

    posts = Post.objects.filter(parent_board=currentboard).order_by('-id')

    
    context = {
        'form':form,
        'posts':posts,
        'board':currentboard,
    }
    return render(request, 'boards/board.html', context)

def viewthread(request):


    pass
