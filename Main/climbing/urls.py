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
    path('list/detail/<int:pk>/', views.postlist_detail, name='list_detail'),
    path('list/post/', views.postlist_post, name='list_post'),

    # Record
    path('record/', views.record, name='record'),

    # My list
    path('mylist/', views.mylist_main, name='mylist_main'),
    path('mylist/<int:pk>/', views.mylist_detail, name='mylist_detail'),
    path('mylist/<int:pk>/delete', views.mylist_delete, name='mylist_delete'),

    # Friend
    path('friend/', views.friend_main, name='friend_main'),
    path('friend/<int:friend_id>/', views.friend_detail, name='friend_detail'),

    # etc
    path('error/', views.errorpage, name='error'),
]