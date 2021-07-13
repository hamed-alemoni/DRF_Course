from rest_framework import serializers
from blog.models import Article


# create first serializer
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ['updated']
