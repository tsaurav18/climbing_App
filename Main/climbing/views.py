from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

# from google.cloud import storage

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


# 메인 페이지
def main(request):
    posts = PostMountain.objects.get(id=1)
    context = {
        'mountain_of_month' : posts.imgpath
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
    return render(request, 'list_detail_view.html', {'post': post})


# 산 글쓰기 페이지
def postlist_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user_id = Account.objects.get(username=request.user.get_username())
            temp.save()
            return redirect('list_main')
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
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # target.imgpath = form.cleaned_data['']
            target.name = form.cleaned_data['name']
            target.body = form.cleaned_data['body']
            target.star = form.cleaned_data['star']
            target.save()
            return redirect('/detail/' + str(target.pk))
    else:
        form = PostForm()
        return render(request, 'list_post_view.html', {'form': form})


# 산 글쓰기 삭제
def postlist_delete(request, pk):
    target = MyList.objects.get(id=pk)
    target.delete()
    return redirect('list_main')


# gcs에 파일 업로드 및 linkurl 반환
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )


# 등산 기록 페이지
def record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mylist_main')
        else:
            return redirect('error')
    else:
        form = RecordForm()
        return render(request, 'record.html', {'form': form})
    # return render(request, 'record.html')


# 개인 등산 목록 페이지
def mylist_main(request):
    now_id = Account.objects.get(username=request.user.get_username()).id
    mylist = MyList.objects.filter(user_id=now_id)
    context = {
        'mylist': mylist
    }
    return render(request, 'mylist_main.html', context)


# 개인 등산 상세 페이지
def mylist_detail(request, pk):
    mine = get_object_or_404(MyList, pk=pk)
    return render(request, 'mylist_detail.html', {'mine' : mine})


# 개인 등산 리스트 삭제
def mylist_delete(request, pk):
    target = MyList.objects.get(id=pk)
    target.delete()
    return redirect('mylist_main')


# 개인 등산 리스트 수정
def mylist_edit(request, pk):
    target = MyList.objects.get(id=pk)
    pass
    return redirect('mylist_main')


# 친구 추천 페이지
def friend_main(request):
    return render(request, 'friend.html')


# 친구 상세 페이지
def friend_detail(request):
    return render(request, 'friend_detail.html')


# 에러 메세지 내는 페이지
def errorpage(request):
    return render(request, 'errorpage.html', {})
