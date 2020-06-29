from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

# from google.cloud import storage

import smtplib
from email.mime.text import MIMEText

import os, tempfile

from .forms import *
from .models import *


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = Account.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('main')
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return HttpResponse('로그인 실패')
    else:
        form = SigninForm()
        return render(request, 'signin.html', {'form': form})


def logout(request):
    return redirect('/')


# 메인 페이지
def main(request):
    posts = PostMountain.objects.get(id=1)
    context = {
        'mountain_of_month': posts
    }
    return render(request, 'main.html', context)


# 산 리스트 메인페이지
def postlist_main(request):
    first_posts = PostMountain.objects.get(id=1)
    second_posts = PostMountain.objects.get(id=2)
    others = PostMountain.objects.order_by('date')
    context = {
        'mountain_of_month': first_posts,
        'recomend_mountain': second_posts,
        'others': others[2::-1]
    }
    return render(request, 'list_main.html', context)


# 산 디테일 페이지
def postlist_detail(request, pk):
    post = get_object_or_404(PostMountain, pk=pk)
    now_user = Account.objects.get(username=request.user.get_username())
    return render(request, 'list_detail_view.html', {'post': post, 'now_user': now_user})


# 산 글쓰기 페이지
def postlist_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user_id = Account.objects.get(username=request.user.get_username())
            temp.save()
            imgpath = '.'+PostMountain.objects.get(id=temp.id).img.url
            # temp.imgpath = upload_file_gcs(imgpath, 'Postimgs/test.jpg')
            print('이미지 업로드 성공')
            temp.save()
            return redirect('list_detail', pk=temp.id)
        else:
            return redirect('error')
    else:
        form = PostForm()
        return render(request, 'list_post_view.html', {'form': form})


# 산 글쓰기 수정
def postlist_edit(request, pk):
    target = PostMountain.objects.get(id=pk)
    # 글을 수정사항을 입력하고 제출을 눌렀을 때
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # target.imgpath = form.cleaned_data['']
            target.name = form.cleaned_data['name']
            target.body = form.cleaned_data['body']
            target.star = form.cleaned_data['star']
            target.save()
            return redirect('list_detail', pk=pk)
    else:
        form = PostForm(instance=target)
        return render(request, 'list_post_view.html', {'form': form})


# 산 글쓰기 삭제
def postlist_delete(request, pk):
    target = PostMountain.objects.get(id=pk)
    target.delete()
    return redirect('list_main')


# # gcs에 파일 업로드 및 linkurl 반환
# def upload_file_gcs(img_dir, destination_blob_name, bucket_name='climbing_storage'):
#     # file_name : 업로드할 파일명
#     # destination_blob_name : 업로드될 경로와 파일명
#     # bucket_name : 업로드할 버킷명
#
#     file_name = open(img_dir, 'rb')  # 업로드할 이미지의 파일 객체
#
#     try:
#         # upload img
#         storage_client = storage.Client()
#         bucket = storage_client.get_bucket(bucket_name)
#         blob = bucket.blob(destination_blob_name)
#         blob.upload_from_file(file_name)
#     except Exception as ex:
#         print('upload :', ex)
#
#     try:
#         # get url from gcs
#         bucket_get = storage_client.bucket(bucket_name)
#         blob_get = bucket_get.blob(destination_blob_name)
#         return blob_get.public_url
#     except Exception as ex:
#         print('get url : ', ex)


# 등산 기록 페이지
def record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user_id = Account.objects.get(username=request.user.get_username())
            temp.save()
            return redirect('mylist_main')
        else:
            return redirect('error')
    else:
        form = RecordForm()
        form2 = Record2Form()
        return render(request, 'record.html', {'form': form, 'form2': form2})


# 개인 등산 목록 페이지
def mylist_main(request):
    now_id = Account.objects.get(username=request.user.get_username()).id
    mylist = MyList.objects.filter(user_id=now_id).order_by('-date')
    context = {
        'mylist': mylist
    }
    return render(request, 'mylist_main.html', context)


# 개인 등산 상세 페이지
def mylist_detail(request, pk):
    mine = get_object_or_404(MyList, pk=pk)
    return render(request, 'mylist_detail.html', {'mine': mine})


# 개인 등산 리스트 삭제
def mylist_delete(request, pk):
    target = MyList.objects.get(id=pk)
    target.delete()
    return redirect('mylist_main')


# # 개인 등산 리스트 수정
# def mylist_edit(request, pk):
#     target = MyList.objects.get(id=pk)
#     if request.method == "POST":
#         form = RecordForm(request.POST)
#         if form.is_valid():
#             target.m_name = form.cleaned_data['m_name']
#             target.course = form.cleaned_data['course']
#             target.time = form.cleaned_data['time']
#             target.save()
#             return redirect('/detail/' + str(target.pk))
#     else:
#         form = RecordForm(instance=target)
#         return render(request, 'mylsit_edit.html', {'form': form})


# 친구 추천 페이지
def friend_main(request):
    Users = Account.objects.all()
    context = {
        'Users': Users[1:]
    }
    return render(request, 'friend.html', context)


# 친구 상세 페이지
def friend_detail(request):
    return render(request, 'friend_detail.html')


# 친구 상세 페이지
def friend_sendmail(request, pk):
    now_me = Account.objects.get(username=request.user.get_username())
    target = Account.objects.get(id=pk)

    try:
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login('dev.ksanbal@gmail.com', 'jkybizzwutfgwstn')

        msg = MIMEText('''
            Climbinb
            
            안녕하세요 {}님!
            {}님이 당신과 연락하고 싶어합니다!
            {}로 메일을 보내 대화해보세요!!
        '''.format(target.username, now_me.username, now_me.email))
        msg['Subject'] = 'Climbing - 누군가 당신과 연락하고 싶어해요!'
        session.sendmail('Climbing@gmail.com', target.email, msg.as_string())

        context = {
            'issuccess': True
        }
        return render(request, 'friend_main', context)
    except Exception as ex:
        print('HEY!', ex)
        return redirect('friend_main')


# 에러 메세지 내는 페이지
def errorpage(request):
    return render(request, 'errorpage.html', {})
