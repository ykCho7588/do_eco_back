import django
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


# Create your views here.
##from here
'''
def sign_up(request):
    if request.method == 'GET':
        return render(request, '/signup.html')
    elif request.method == 'POST':  # 회원가입 정보 입력 후 가입하기 클릭시
        username = request.POST.get('username', None)  # 이름
        password = request.POST.get('password', None)  # 비밀번호
        password2 = request.POST.get('password2', None)  # 비밀번호 확인
        #bio = request.POST.get('bio', None)  # 자기소개

        if password != password2:  # 비밀번호와 비밀번호 확인이 같지 않으면
            return render(request, 'user/signup.html')  # 페이지 다시 로드
        
        else:  # 같으면
            exist_user = get_user_model().objects.filter(username=username)  # 같은 이름의 사용자가 있는지 데이터베이스 조회

            if exist_user:  # 이미 있다면
                return render(request, 'user/signup.html')  # 페이지 다시 로드
            else:  # 없다면
                User.objects.create_user(username=username, password=password)  # 데이터베이스에 이름, 비밀번호, 자기소개를 저장
                return redirect('/login')  # 로그인 페이지로 이동
'''
##to here


def login(request):
    # POST 요청이 들어오면 로그인 처리를 함
    if request.method == 'POST':
        # POST 요청하는 데이터 username으로 담아줌
        userid = request.POST['username']
        # POST 요청하는 데이터 password로 담아줌
        pwd = request.POST['password']

        # 실제로 데이터베이스에 있는 회원인지 username과 password로 확인
        user = auth.authenticate(request, username = userid, password = pwd)

        # 이미 user 가 있다면
        if user is not None:
            # 해당 객체로 로그인
            auth.login(request,user)
            # home 화면으로 redirect
            # 프론트 코드와 머지하면 바꾸기(홈화면 링크로)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect'})
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)

