from django.contrib import admin
from django.urls import path
from .views import title_list,postuser,edit,RegisterAPI, LoginAPI, LogoutAPI,UserList,CreateVote,Vote_check,changeVote,no_of_vote
from knox import views as knox_views

urlpatterns = [
    path('list/',title_list),
    path('list/<str:pk>/',postuser.as_view(),name = 'post all blog posted'),
    path('list/edit/<int:pk>/',edit),

    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', LogoutAPI.as_view(), name='logout'),
    path('users/', UserList.as_view(), name='user-list'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    path('vote/',CreateVote.as_view(),name='Create new vote'),
    path('vote/<str:pk>/<str:b>/',Vote_check.as_view(),name='check user vote'),
    path('change/vote/<str:pk>/',changeVote,name='change vote && delete'),
    path('vote/count/<str:pk>',no_of_vote.as_view(),name='count vote for blog')

]
