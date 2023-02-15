from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from django.http.response import JsonResponse

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .serializers import TableSerializer
from .models import Table

#from .viewset import UserViewSet

@api_view(['GET','POST'])
def title_list(request):
    if request.method == 'GET':
        titles = Table.objects.all()  #complex data
        serializer = TableSerializer(titles,many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class postuser(generics.ListAPIView):
    serializer_class = TableSerializer
    def get_queryset(self):
        User = self.kwargs['pk']
        return Table.objects.filter(User= User)

@api_view(['GET', 'PUT', 'DELETE'])
def edit(request,pk):
    try:
        table = Table.objects.get(pk=pk)
    except Table.DoesNotExist:
        return JsonResponse({'message':'It does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        table_serializer = TableSerializer(table)
        return JsonResponse(table_serializer.data)

    elif request.method == 'PUT':
        table_data = JSONParser().parse(request)
        table_serializer = TableSerializer(table, data=table_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse(table_serializer.data)
        return JsonResponse(table_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method =='DELETE':
        table.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

