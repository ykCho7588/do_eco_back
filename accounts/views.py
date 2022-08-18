import django
from django.shortcuts import render, redirect
from django.contrib import auth

from django.contrib.auth.models import User


# Create your views here.


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
  
        else:
            return render(request, 'login.html')


def logout(request):
    auth.logout(request)

