from unicodedata import category
import django_filters

from reviews.models import Title


class TitleFilter(django_filters.FilterSet):
    genre = django_filters.CharFilter(field_name='genre', lookup_expr='iexact')
    category = django_filters.CharFilter(field_name='category',
                                         lookup_expr='iexact')
    year = django_filters.NumberFilter(field_name='year', lookup_expr='iexact')
    name = django_filters.CharFilter(field_name='name', lookup_expr='iexact')

    class Meta:
        model = Title
        fields = ('genre', 'category', 'year', 'name')
