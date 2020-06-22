from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
            return redirect('errorpage')
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            print(request.POST)
            try:
                model = Account(username=request.POST['username'])
            except Exception as ex:
                print(ex)

            return redirect('main')
        else:
            return redirect('errorpage')
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
    context = {
        'mountain_of_month': first_posts.imgpath,
        'recomend_mountain': second_posts.imgpath
    }
    return render(request, 'list_main.html', context)


# 산 디테일 페이지
def postlist_detail(request):
    return render(request, 'list_detail_view.html')


# 산 글쓰기 페이지
def postlist_post(request):
    form = PostForm()
    return render(request, 'list_post_view.html', {'form':form})


# 등산 기록 페이지
def record(request):
    return render(request, 'record.html')


# 개인 등산 목록 페이지
def mylist_main(request):
    return render(request, 'mylist.html')


# 개인 등산 상세 페이지
def mylist_detail(request):
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
