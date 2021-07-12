
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
)

from core.serializers import (
    UserRegistrationSerializer,
    PostSerializer,
)
from core.models import Post
from core.filters import PostFilter
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)


@extend_schema_view(
    create=extend_schema(
        operation_id='User Registration',
        auth=[{}],
        parameters=[UserRegistrationSerializer],
    ),

)
class UserRegistrationViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = UserRegistrationSerializer
    permission_classes = []


@extend_schema_view(
    create=extend_schema(
        operation_id='Create Post',
    ),
    list=extend_schema(
        operation_id='List Post',
    ),

)
class PostViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
):
    serializer_class = PostSerializer
    filterset_class = PostFilter
    permission_classes = [IsAuthenticated]
    ordering_fields = ['create_date']
    parser_classes = (MultiPartParser,)

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
