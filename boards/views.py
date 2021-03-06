from django.shortcuts import render, redirect
from .models import Board, Comment
from pprint import pprint
# Create your views here.

def jndex(request):
    boards = Board.objects.order_by('-pk')
    context = {
        'boards' : boards,
    }
    return render(request, 'boards/jndex.html', context)
def index(request):
    # pprint(request)
    # pprint(type(request))
    # pprint(dir(request))
    # pprint(request.scheme)
    # pprint(request.get_host())
    # pprint(request.get_full_path())
    # pprint(request.build_absolute_uri)
    # pprint(request.META)
    # print()
    # pprint(request.method)
    boards = Board.objects.order_by('-pk')
    context = {
        'boards' : boards,
    }
    return render(request, 'boards/index.html', context)
    
def new(request):
    #NEW
    if request.method == 'GET':
        return render(request, 'boards/new.html')
    #CREATE
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        board = Board(title=title, content=content)
        board.save()
        return redirect('boards:detail', board.pk)
    
def detail(request,board_pk):
    board = Board.objects.get(pk=board_pk)
    comments = board.comment_set.all()
    context = {
        'board': board,
        'comments': comments,
    }
    return render(request, 'boards/detail.html', context)
    
def delete(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:detail', board.pk)
        
def edit(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    #UPDATE
    if request.method == 'POST':
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail', board.pk)
    #EDIT
    else:    
        context = {
            'board' : board,
        }
        return render(request, 'boards/edit.html', context)

def comments_create(request, board_pk):
    #댓글을 달 게시물
    board = Board.objects.get(pk=board_pk)
    
    # form 에서 넘어온 comment data
    content = request.POST.get('content')
    
    #댓글 생성 및 저장
    comment = Comment(board=board, content=content)
    comment.save()
    return redirect('boards:detail', board.pk)
    
def comments_delete(request, board_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('boards:detail', board_pk)
    else:
        return redirect('boards:detail', board_pk)
        