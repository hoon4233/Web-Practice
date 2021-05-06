from django.shortcuts import render, redirect

from member.models import BoardMember
from .models import Board
from .forms import BoardForm

from django.http import Http404

from django.core.paginator import Paginator

# Create your views here.

def board_list(request):
    if request.method == 'POST':
        return redirect('/board/write/')
    all_boards = Board.objects.all().order_by('-id')  #앞에 -가 붙으면 역순으로 가져온다는 거임
    page = int(request.GET.get('p',1))  # p라는 값을 받을 거고 없으면 1로
    pagenator = Paginator(all_boards,2)  # boards를 가져와서 1페이지에 2개의 object씩 보이도록 설정함
    boards = pagenator.get_page(page)
    return render(request, 'board_list.html', {'boards':boards})

def board_write(request):
    if not request.session.get('user'):
        return redirect('/member/login/')
        
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid() :
            user_id = request.session.get('user')
            member = BoardMember.objects.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.content = form.cleaned_data['contents']
            board.writer = member

            board.save()

            return redirect('/board/list/')

    else :
        form = BoardForm()

    return render(request, 'board_write.html',{'form':form})


def board_detail(request, pk):
    try :
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')

    return render(request, 'board_detail.html',{'board':board})