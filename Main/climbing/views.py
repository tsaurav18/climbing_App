from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

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
    form = PostForm()
    return render(request, 'list_post_view.html', {'form': form})


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
    mylist = MyList.objects.order_by('date')
    context = {
        'mylist': mylist
    }
    return render(request, 'mylist.html', context)


# 개인 등산 상세 페이지
def mylist_detail(request, id):
    return render(request, 'mylist_detail.html')


# 친구 추천 페이지
def friend_main(request):
    return render(request, 'friend.html')


# 친구 상세 페이지
def friend_detail(request):
    return render(request, 'friend_detail.html')


# 에러 메세지 내는 페이지
def errorpage(request):
    return render(request, 'errorpage.html', {})
