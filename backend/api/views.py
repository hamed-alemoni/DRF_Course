from django.shortcuts import render




# Create your views here.
# first view to make info serialize
from rest_framework.generics import ListAPIView,ListCreateAPIView

from .serializers import ArticleSerializer
from blog.models import Article


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
