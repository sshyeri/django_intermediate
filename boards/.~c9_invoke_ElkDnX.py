from django.shortcuts import render, redirect
from .models import Board
from pprint import pprint
# Create your views here.

def index(request):
    pprint(request)
    pprint(type(request))
    pprint(dir(request))
    pprint(request.scheme)
    pprint(request.get_host())
    pprint(request.get_full_path())
    pprint
    p
    
    
    boards = Board.objects.order_by('-pk')
    context = {
        'boards' : boards,
    }
    return render(request, 'boards/index.html', context)
    
def new(request):

    return render(request, 'boards/new.html')
    
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    board = Board(title=title, content=content)
    board.save()
    return redirect('boards:detail', board.pk)
    
def detail(request, pk):
    board = Board.objects.get(pk=pk)
    context = {
        'board': board,
    }
    return render(request, 'boards/detail.html', context)
    
def delete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('boards:index')
    
def edit(request, pk):
    board = Board.objects.get(pk=pk)
    context = {
        'board' : board,
    }
    return render(request, 'boards/edit.html', context)
    
def update(request, pk):
    board = Board.objects.get(pk=pk)
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    return redirect('boards:detail', board.pk)