from django.urls import include, path, re_path
from rest_framework.routers import SimpleRouter
from core.views import PostViewSet, UserRegistrationViewSet

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
)


router = SimpleRouter()

router.register(
    'post',
    PostViewSet,
    basename='post',
)
router.register(
    'user/register',
    UserRegistrationViewSet,
    basename='user-register',
)


urlpatterns = [
    path('', include(router.urls)),
    re_path('^user/login/?$',
            TokenObtainPairView.as_view(),
            name='token_obtain_pair',
            ),
    re_path('^user/login/refresh/?$',
            TokenRefreshView.as_view(),
            name='token_refresh',
            ),
]
