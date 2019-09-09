from rest_framework import serializers
from .models import Publisher, Books


class PublisherSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Publisher
        fields = '__all__'


class BooksSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Books
        fields = (
            'id',
            'title',
            'publisher'
        )