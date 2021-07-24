from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ArticleSerializer, UserSerializer
from blog.models import Article
from .permissions import IsSuperuserOrAuthorReadOnly, IsStaffOrReadOnly, IsAuthorOrReadOnly
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

# a view to make all objects info serialize
# get objects
# create new object
class ArticleList(ListCreateAPIView):
    # get all articles
    queryset = Article.objects.all()
    # determine serializer class
    serializer_class = ArticleSerializer
    # add a new permission for this view
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


# a view to make an object info serialize
# retrieve object
# update object
# destroy object
class ArticleDetail(RetrieveUpdateDestroyAPIView):
    # get all articles
    queryset = Article.objects.all()
    # determine serializer class
    serializer_class = ArticleSerializer
    # add a new permission for this view
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


# a view to make all objects info serialize
# get objects
# create new object
class UserList(ListCreateAPIView):
    # get all articles
    queryset = User.objects.all()
    # determine serializer class
    serializer_class = UserSerializer
    # add a new permission for this view
    permission_classes = (IsSuperuserOrAuthorReadOnly,)


# a view to make an object info serialize
# retrieve object
# update object
# destroy object
class UserDetail(RetrieveUpdateDestroyAPIView):
    # get all articles
    queryset = User.objects.all()
    # determine serializer class
    serializer_class = UserSerializer
    # add a new permission for this view
    permission_classes = (IsSuperuserOrAuthorReadOnly,)


# To revoke tokens
class RevokeToken(APIView):
    # add a new permission for this view
    permission_classes = (IsAuthenticated,)

    # delete the token
    def delete(self, request):
        request.auth.delete()
        return Response(status=204)
