import django
from django.shortcuts import render, redirect
from django.contrib import auth

from django.contrib.auth.models import User


# Create your views here.

#로그인/로그아웃
def login(request):
    # POST 요청이 들어오면 로그인 처리를 함
    if request.method == 'POST':
        # POST 요청하는 데이터 username으로 담아줌
        userid = request.POST.get('username')
        # POST 요청하는 데이터 password로 담아줌
        pwd = request.POST.get('password')

        # 실제로 데이터베이스에 있는 회원인지 username과 password로 확인
        user = auth.authenticate(request, username = userid, password = pwd)

        # 이미 user 가 있다면
        if user is not None:
            # 해당 객체로 로그인
            auth.login(request,user)
            # home 화면으로 redirect
            # 프론트 코드와 머지하면 바꾸기(홈화면 링크로)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect'})

    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)

#회원가입
def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['repeat']:
            # 회원가입
            new_user = User.objects.create_user(username=request.POST['username'] , password= request.POST['password'])
            # 로그인
            auth.login(request, new_user)
            # 방금 회원가입한 new_user 로 로그인
            # 홈 리다이렉션
            return redirect('main')
    return render(request, 'register.html')

