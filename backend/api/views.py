from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .serializers import ArticleSerializer
from blog.models import Article


# Create your views here.

# first view to make info serialize
class ArticleList(ListCreateAPIView):
    # get all articles
    queryset = Article.objects.all()
    # determine serializer class
    serializer_class = ArticleSerializer
