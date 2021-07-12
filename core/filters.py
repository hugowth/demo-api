from django_filters import CharFilter, rest_framework as filters

from core.models import Post


class PostFilter(filters.FilterSet):
    username = CharFilter(
        field_name='created_by__username',
        lookup_expr='exact',
    )

    class Meta:
        model = Post
        fields = [
            'username'
        ]
