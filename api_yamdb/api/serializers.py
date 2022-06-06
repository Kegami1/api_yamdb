from datetime import datetime
from django.db.models import Avg
from os import set_inheritable
from xml.dom import ValidationErr
from rest_framework import serializers

from reviews.models import Review, Comment, Category, Title, Genre


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    score = serializers.IntegerField(min_value=1, max_value=10)

    def validate(self, obj):
        title_id = self.context['view'].kwargs.get('title_id')
        user = self.context['request'].user
        not_first_review = Review.objects.filter(
            title=title_id,
            author=user
        ).exists()
        if self.context['request'].method == 'POST' and not_first_review:
            raise serializers.ValidationError('Вы уже оставляли рецензию')
        return obj

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitleSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField(read_only=True)
    genre = serializers.SlugRelatedField(many=True,
                                         slug_field='slug',
                                         queryset=Genre.objects.all())
    category = serializers.SlugRelatedField(slug_field='slug',
                                            queryset=Category.objects.all())                          
    year = serializers.IntegerField()

    def get_rating(self, obj):
        value = Review.objects.filter(
            title=obj.id
        ).aggregate(rating=Avg('score'))
        return value['rating']

    def validate_year(self, value):
        if value >= datetime.now().year:
            raise serializers.ValidationError('Нельзя добавить произведение которое ещё не вышло')
        return value


    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description', 'rating', 'genre',
                  'category')

    
class TitleGetSerializer(serializers.ModelSerializer):
    # genre = serializers.SlugRelatedField(many=True,
    #                                      slug_field='slug',
    #                                      queryset=Genre.objects.all())
    # category = serializers.SlugRelatedField(slug_field='slug',
    #                                         queryset=Category.objects.all())                          
    category = CategorySerializer(many=False)
    genre = GenreSerializer(many=True)
    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description', 'genre',
                  'category')

