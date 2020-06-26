from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),

    # Main
    path('main/', views.main, name='main'),

    # list
    path('list/', views.postlist_main, name='list_main'),
    path('list/detail/<int:list_id>/', views.postlist_detail, name='list_detail'),
    path('list/post/', views.postlist_post, name='list_post'),

    # Record
    path('record/', views.record, name='record'),

    # My list
    path('mylist/', views.mylist_main, name='mylist_main'),
    path('mylist/<int:mylist_id>/', views.mylist_detail, name='mylist_detail'),

    # Friend
    path('friend/', views.friend_main, name='friend_main'),
    path('friend/<int:friend_id>/', views.friend_detail, name='friend_detail'),

    # etc
    path('error/', views.errorpage, name='error'),
]