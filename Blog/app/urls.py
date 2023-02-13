
from django.contrib import admin
from django.urls import path
from .views import title_list,postuser,update,edit


urlpatterns = [
    path('list/',title_list),
    path('list/update/<int:pk>',update),
    path('list/<str:pk>/',postuser.as_view(),name = 'detailcreate'),
    path('list/edit/<int:pk>',edit)
]

