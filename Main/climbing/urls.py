from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Auth
    path('', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),

    # Main
    path('main/', views.main, name='main'),

    # list
    path('list/', views.postlist_main, name='list_main'),
    path('list/detail/<int:pk>/', views.postlist_detail, name='list_detail'),
    path('list/detail/<int:pk>/delete/', views.postlist_delete, name='list_delete'),
    path('list/detail/<int:pk>/edit/', views.postlist_edit, name='list_edit'),
    path('list/post/', views.postlist_post, name='list_post'),

    # Record
    path('record/', views.record, name='record'),

    # My list
    path('mylist/', views.mylist_main, name='mylist_main'),
    path('mylist/<int:pk>/', views.mylist_detail, name='mylist_detail'),
    path('mylist/<int:pk>/delete', views.mylist_delete, name='mylist_delete'),
    # path('mylist/<int:pk>/edit', views.mylist_edit, name='mylist_edit'),

    # Friend
    path('friend/', views.friend_main, name='friend_main'),
    path('friend/<int:friend_id>/', views.friend_detail, name='friend_detail'),
    path('friend/<int:pk>/sendmail/', views.friend_sendmail, name='friend_sendmail'),

    # etc
    path('error/', views.errorpage, name='error'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)