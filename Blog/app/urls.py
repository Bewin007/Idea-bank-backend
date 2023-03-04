from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import title_list,postuser,edit,LoginAPI,RegisterAPI,postregisterdetail,PostVote
from knox import views as knox_views

urlpatterns = [
    path('list/',title_list),
    path('list/<str:pk>/',postuser.as_view(),name = 'detailcreate'),
    path('list/edit/<int:pk>/',edit),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('regestered/', postregisterdetail),
    path('api/<int:pk>/vote/',PostVote.as_view(), name ='post_vote')
]
