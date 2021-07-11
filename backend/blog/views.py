from django.shortcuts import render
from .models import Article
from django.views.generic import ListView


# Create your views here.

class ArticleList(ListView):
    # article view to show info of articles
    def get_queryset(self):
        return Article.objects.filter(status=True)
