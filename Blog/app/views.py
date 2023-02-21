from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib.auth import login

from rest_framework import generics, permissions
from rest_framework import status
from rest_framework import permissions

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView

from .serializers import TableSerializer,UserSerializer,RegisterSerializer
from .models import Table,User

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

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "email": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

@api_view(['GET'])
def postregisterdetail(request):
    if request.method == 'GET':
        titles = User.objects.all()  #complex data
        serializer = UserSerializer(titles,many = True)
        return Response(serializer.data)


class PostVote(generics.UpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    def voting(self,request,*args,**kwargs):
        post = self.get_object()
        vote_type = request.data.get('vote_type')
        if vote_type =='upvote':
            post.Upvote +=1
        elif vote_type == 'downvote':
            post.Downvote +=1
        post.save()
        serializer = self.get_serializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
