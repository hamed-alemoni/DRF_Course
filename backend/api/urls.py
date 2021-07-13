from django.urls import path, include
from .views import ArticleList

app_name = 'aoi'

urlpatterns = [
    path('', ArticleList.as_view(), name='list')
]
