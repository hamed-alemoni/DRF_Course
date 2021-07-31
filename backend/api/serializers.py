from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model


# create a serializer for Article module
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ['updated']


# create a serializer for User module
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
