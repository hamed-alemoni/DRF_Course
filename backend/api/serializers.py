from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model
from drf_dynamic_fields import DynamicFieldsMixin


# create a class to make particular author's data and return it
class AuthorUsernameField(serializers.RelatedField):
    # first way
    def to_representation(self, value):
        return value.username


# create a serializer for Article module
class ArticleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    # return author's detail
    def get_author(self, obj):
        return {
            'ID': obj.author.pk,
            'Username': obj.author.username
        }

    # third way
    author = serializers.SerializerMethodField('get_author')

    # second way
    # author = serializers.CharField(source='author.username',read_only=True)

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
