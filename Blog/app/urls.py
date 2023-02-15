
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import title_list,postuser,edit


urlpatterns = [
    path('list/',title_list),
    path('list/<str:pk>/',postuser.as_view(),name = 'detailcreate'),
    path('list/edit/<int:pk>',edit)
]
