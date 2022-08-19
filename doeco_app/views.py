
from dataclasses import field
import re
from time import timezone
from urllib import request
from webbrowser import get
from django.shortcuts import render, get_object_or_404, redirect
import requests
import json
from .models import Ecospot, FreePost, FreeComment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
from .forms import *


def main(request):
        return render(request, 'main.html')

#지도
def Ecospots(request):
        ecospots = Ecospot.objects.all
        return render(request, 'ecospot.html', {'ecospots':ecospots})

#자유게시판 홈
def freehome(request):
        freeposts = FreePost.objects.all()

        #freeposts = FreePost.objects.filter().order_by('-date')
        return render(request, 'free_index.html', {'freeposts' : freeposts})

#게시물 작성

def freepostcreate(request):
        if request.method == "POST" or request.method == "FILES":
                new_post = FreePostForm(request.POST, request.FILES)
                if new_post.is_valid():
                        a =new_post.save(commit=False) 
                        a.author = request.user
                        #a.photo = request.photo
                        a.save()
        #new_post.date = request.POST.get('date')
                        return redirect('freehome')
        else:
                a = FreePostForm()
        return render(request, 'free_post_form.html' , {'a' : a})

#게시물 detail
def freedetail(request, post_id):
        post_detail = get_object_or_404(FreePost, pk=post_id)
    # FreePost 로부터 2번째 인자인 pk로 받은 해당 게시물 글을 갖고와라
        comment_form = FreeCommentForm()
    # 댓글 기능 띄워주기
        return render(request, 'free_detail.html', {'post_detail' : post_detail, 'comment_form' : comment_form})

#게시물 삭제
def freepostdelete(request, post_id):
        post_delete = get_object_or_404(FreePost, pk=post_id)
        post_delete.delete()
        return render(request, 'free_index.html')

#게시물 수정
def freepostupdate(request, post_id):
        post_update= get_object_or_404(FreePost, pk=post_id)

        post_update.title = request.POST['title']
        post_update.body = request.POST['body']
        post_update.date = timezone.now()
        post_update.author = request.POST['author']
        
        post_update.save()
        return redirect('free_detail.html' , post_update.id)

#댓글 작성
def new_freecomment(request, post_id):
    filled_form = FreeCommentForm(request.POST)
    # FreeCommentForm 띄워라
    if filled_form.is_valid():
        #바로 저장하지 않고
        finished_form = filled_form.save(commit=False)
        # 어떤 게시물에 대한 댓글인지 정해지지 않았으므로 일단 저장하지 않고
        finished_form.post = get_object_or_404(FreePost, pk = post_id)
        # finished_form의 post에 get_object_or_404 -> 어떤 게시물에 대한 댓글인 지 확인 후
        finished_form.save()  
    return redirect('freedetail', post_id)

#댓글 삭제
def new_freecomment_delete(request, post_id, comment_id):
        post_detail = get_object_or_404(FreePost, pk=post_id)
        comment_form = FreeCommentForm()
        if request.user.is_authenticated:
                comment = get_object_or_404(FreeComment, pk=comment_id)
                if request.user == comment.user:
                        comment.delete()
        return redirect('free_detail.html',post_id, {'post_detail' : post_detail, 'comment_form' : comment_form} )

#댓글 수정



def Mypage(request):
        return render(request, "Mypage.html")


def ecorank(request):
        return render(request, 'eco-rank.html')


def ecotip(request):
        return render(request, 'EcoTip.html')

def zeroshop(request):
        return render(request, 'G9shop.html')

def ecospot(request):
        return render(request, 'ecospot.html')