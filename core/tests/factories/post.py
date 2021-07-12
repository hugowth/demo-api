import factory
from core.models import Post


class PostFactory(factory.django.DjangoModelFactory):
    description = 'test'
    created_by = factory.SubFactory('core.tests.factories.user.UserFactory')

    class Meta:
        model = Post
