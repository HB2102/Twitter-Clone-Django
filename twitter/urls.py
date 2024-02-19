from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('tweet_like/<int:pk>', views.tweet_like, name='tweet_like'),
    path('tweet_show/<int:pk>', views.tweet_show, name='tweet_show'),
    path('profile/followers/<int:pk>', views.followers, name='followers'),
    path('profile/follows/<int:pk>', views.follows, name='follows'),
    path('delete_tweet/<int:pk>', views.delete_tweet, name='delete_tweet'),
    path('edit_tweet/<int:pk>', views.edit_tweet, name='edit_tweet'),
    path('search/', views.search, name='search'),
    path('search_user/', views.search_user, name='search_user'),
]
