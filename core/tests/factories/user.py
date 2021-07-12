import factory
import uuid

from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    password = 'podafgkpodfg'  # nosec
    username = factory.LazyAttribute(lambda x: uuid.uuid4())

    class Meta:
        model = User
