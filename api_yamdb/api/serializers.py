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
  
    class Meta: 
        model = Title
        fields = ('name', 'year', 'description', 'genre', 'category')

