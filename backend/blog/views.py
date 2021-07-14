from django.shortcuts import render, get_object_or_404
from .models import Article
from django.views.generic import ListView, DetailView


# Create your views here.

class ArticleList(ListView):
    # article view to show info of articles
    def get_queryset(self):
        return Article.objects.filter(status=True)


# this class base view show a special article
class ArticleDetail(DetailView):
    # get our special article
    def get_object(self):
        return get_object_or_404(Article.objects.filter(status=True), pk=self.kwargs.get('pk'))
