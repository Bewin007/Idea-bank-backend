from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet,ViewSet
from .models import Table
from .serializers import TableSerializer

class TableViewSet(ViewSet.ModelViewSet):
    queryset = Table.objects.all()
