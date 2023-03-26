from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth import get_user_model

from rest_framework import generics, permissions
from rest_framework import status
from rest_framework import permissions

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated

from knox.views import LoginView as KnoxLoginView
from knox.views import LogoutView as KnoxLogoutView
from knox.models import AuthToken

from .serializers import TableSerializer,UserSerializer,VoteSerializer
from .models import Table,User,Vote



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
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

# Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        response_data = super(LoginAPI, self).post(request, format=None)
        response_data.data['user_id'] = user.id
        return response_data


# Logout API
class LogoutAPI(KnoxLogoutView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        return super(LogoutAPI, self).post(request, format=None)
    

User = get_user_model()
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Vote
class CreateVote(generics.GenericAPIView):
    
    def post(self,request):
        userid = request.data.get('user')
        blogid = request.data.get('blog_post')

        if Vote.objects.filter(user= userid) and Vote.objects.filter(blog_post= blogid):
            return Response("already exist")
        else:
            serializer = VoteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
    


        
@api_view(['PUT','DELETE','GET'])
def changeVote(request,pk):
    if request.method =='PUT':
        vote = Vote.objects.get(pk=pk)
        data = JSONParser().parse(request)
        serializer = VoteSerializer(vote, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        vote = Vote.objects.get(pk=pk)
        vote.delete()
        return JsonResponse({'message': 'Vote was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

                
    
class Vote_check(generics.ListAPIView):
    serializer_class = VoteSerializer
    def get_queryset(self):
        User = self.kwargs['pk']
        blog = self.kwargs['b']
        return Vote.objects.filter(user= User,blog_post=blog )

class no_of_vote(APIView):
    def get(self,request,pk):
        upvote = Vote.objects.filter(vote_type='U',blog_post =pk).count()
        downvote = Vote.objects.filter(vote_type = 'D',blog_post =pk).count()
        vote_count = {
            'upvotes': upvote,
            'downvotes': downvote,
        }
        return Response(vote_count)       