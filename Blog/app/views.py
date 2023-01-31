from django.shortcuts import render
from .models import Table
# Create your views here.
from .serializers import TableSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

#from .viewset import UserViewSet

@api_view(['GET','POST'])
def title_list(request):
    if request.method == 'GET':
        titles = Table.objects.all()  #complex data
        serializer = TableSerializer(titles,many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print("dwadwa")
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response(serializer.errors)

# @api_view(['GET'])
# def api(request,pk):
#     print(pk)
#     api = Table.objects.get(pk = Table.User)
#     serializer = TableSerializer(api, many=True)
#     return Response(serializer.data)

class postuser(generics.ListAPIView):
    serializer_class = TableSerializer
    def get_queryset(self):
        User = self.kwargs['pk']
        print(User)
        return Table.objects.filter(User= User)
