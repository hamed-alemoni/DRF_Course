from django.urls import path, include
from .views import UserViewSet, ArticleViewSet
from rest_framework import routers

app_name = 'api'

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'', ArticleViewSet)
urlpatterns = [
    path('', include(router.urls))
]
