from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),

    # Main
    path('main/', views.main, name='main'),

    # list
    path('list/', views.postlist_main, name='listmain'),
    path('list/detail/', views.postlist_detail, name='listdetail'),
    path('list/post/', views.postlist_post, name='listpost'),

    # Record

    # My list

    # Friend

    # etc
    path('error/', views.errorpage, name='error'),
]