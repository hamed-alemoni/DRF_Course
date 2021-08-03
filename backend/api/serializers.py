from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model


# create a serializer for authors
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name', 'last_name']


# create a serializer for Article module
class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedIdentityField(view_name='api:authors-detail')

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ['updated']

    # validate title
    def validate_title(self, value):
        filter_fields = ['javascript', 'laravel', 'php']
        for i in filter_fields:
            if i in value:
                raise serializers.ValidationError(f'Don\'t use this word {i}')


# create a serializer for User module
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
