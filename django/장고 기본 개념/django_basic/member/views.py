from django.shortcuts import render, redirect
from .models import BoardMember
from django.http import HttpResponse  #입력한 비밀번호와 다시 입력한 비밀번호가 다를 때 회원가입을 시키지 않고 에러 메세지를 출력하기 위해 사용
from django.contrib.auth.hashers import make_password, check_password #비밀번호가 입력한 그대로 저장되는 것이 아니라 암호화되어 저장되기 위해 사용, 가져온 row의 pw 값이 입력된 pw 값과 같은지 체크하기 위해 사용
from .forms import LoginForm

def register(request) :
    # 이 register 함수를 부르는 경우의 request는 2가지인데
    # 첫번째로는 주소를 입력해서 들어오는 경우 == GET (로그인 페이지를 보여달라는 요청)
    # 두번째로는 등록버튼을 눌러서 들어오는 경우 == POST (회원가입을 시켜달라는 요청) 
    if request.method == 'GET' :
        return render(request, 'register.html')

    elif request.method == 'POST' :
        # username = request.POST['username']  # 그냥 이렇게 넣으면 별도로 체크해주는 부분이 없으므로 전부 빈칸으로 놓고 회원가입 눌러도 회원가입됨
        username = request.POST.get('username', None)  # 이렇게 해줌으로써 username 이라는 키 값이 없으면 None을 넣어준다. (request가 post 방식이니까 dict 형태로 옴)
        email = request.POST.get('email', None) 
        password = request.POST.get('password', None) 
        re_password = request.POST.get('re_password', None) 

        res_data = {}

        if not (username and password and email and re_password) :
            res_data['error'] = '모든 항목을 입력해야 합니다.'

        elif password != re_password : 
            # return HttpResponse('비밀번호가 다릅니다.') # 그냥 이렇게 return 하면 완전히 새로운 창이 뜨니까 에러 결과를 담고 나중에 render를 return 할때 출력해주자
            res_data['error'] = '비밀번호가 다릅니다.'

        else :
            member = BoardMember(
                username = username,
                password = make_password(password),
                email = email,
            )
            member.save()

        return render(request, 'register.html', res_data) # 이렇게 하면 html 코드로 res_data가 전달되는데 전달되면 끝나는게 아니라 html에서 출력하도록 바꿔줘야함
    
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():  # 기본적으론 form에 빈칸이 없는지 확인해주는 함수, 우리가 forms에 새로운 에러를 추가하면 그것까지 검증해줌 ( ex) 비밀번호가 틀렸는지 )
            request.session['user'] = form.user_id
            return redirect('/')

    elif request.method == 'GET':
        form = LoginForm()

    return render(request, 'login.html',{'form':form})

def logout(request):
    user_id = request.session.get('user')

    if user_id :
        del(request.session['user'])
    
    return redirect('/')