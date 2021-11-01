from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    # These for Serializer superclass
    # title = serializers.CharField(max_length=255)
    # author = serializers.CharField(max_length=255)
    # email = serializers.EmailField(max_length=100)
    # date_added = serializers.DateTimeField()

    # And we can also use ModelSerializer super class
    class Meta:
        model = Article
        fields = ('id', 'title', 'author', 'email')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date_added = validated_data.get('date_added', instance.date_added)
        instance.save()
        return instance

