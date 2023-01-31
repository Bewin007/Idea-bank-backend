
from django.contrib import admin
from django.urls import path
from .views import title_list,postuser


urlpatterns = [
    path('',title_list),
    path('list/',title_list),
    path('list/<str:pk>/',postuser.as_view(),name = 'detailcreate')
]

