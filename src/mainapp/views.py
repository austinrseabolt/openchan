from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NewPostForm
from .models import *
#from .models import * 
def index(request):
    if OpenChan.objects.count() < 1:
        new_oc_instance = OpenChan()
        new_oc_instance.save()
    
    news = News.objects.order_by('-id')
    openchan = OpenChan.objects.get(pk=1)
    posts = Post.objects.filter(parent_post__isnull=True).order_by('-id')
    boards = Board.objects.order_by('board_url')
    if request.user.is_authenticated:
        auth = True
    else:
        auth = False
    context = {
        'openchan':openchan,
        'posts':posts,
        'boards':boards,
        'auth':auth,
        'news':news,
    }
    return render(request, 'boards/index.html', context)


def board(request, boardurl):
    form = NewPostForm(request.POST, request.FILES)
    currentboard = Board.objects.get(board_url=boardurl)
    if request.user.is_authenticated:
        auth = True
    else:
        auth = False
    if request.method == "POST":
       
        if form.is_valid():
            newpost = form.save(commit=False)
            currentboard.post_counter += 1
            newpost.parent_board = currentboard
            newpost.local_id = currentboard.post_counter
            newpost.save()
            currentboard.save()
            return HttpResponseRedirect("/boards/" + str(currentboard.board_url)) #this redirects so you don't resubmit on refresh

    posts = Post.objects.filter(parent_board=currentboard, parent_post__isnull=True).order_by('-id')
    boards = Board.objects.order_by('board_url')
    if OpenChan.objects.count() < 1:
        new_oc_instance = OpenChan()
        new_oc_instance.save()
    openchan = OpenChan.objects.get(pk=1)
    
    context = {
        'form':form,
        'posts':posts,
        'board':currentboard,
        'boards':boards,
        'openchan':openchan,
        'auth':auth,
    }
    return render(request, 'boards/board.html', context)

def ViewThread(request, boardurl, post_pk):
    form = NewPostForm(request.POST, request.FILES)
    op = Post.objects.get(pk=post_pk)
    if request.user.is_authenticated:
        auth = True
    else:
        auth = False
    currentboard = op.parent_board
    boards = Board.objects.order_by('board_url')
    openchan = OpenChan.objects.get(pk=1)
    if request.method == "POST":
        if form.is_valid():
            newpost = form.save(commit=False)
            currentboard.post_counter += 1
            newpost.parent_board = currentboard
            newpost.local_id = currentboard.post_counter
            newpost.parent_post = op
            newpost.save()
            currentboard.save()
            return HttpResponseRedirect("/boards/" + str(currentboard.board_url) +"/" + str(op.pk))
    
    threadreplies = Post.objects.filter(parent_post=op).order_by('id')
    
    context = {
        'op':op,
        'form':form,
        'board':currentboard,
        'boards':boards,
        'openchan':openchan,
        'threadreplies':threadreplies,
        'auth':auth,

    }

    return render(request, 'boards/viewthread.html', context)

