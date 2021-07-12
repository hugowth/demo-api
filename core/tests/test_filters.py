from django.test import TestCase
from core.filters import PostFilter
from core.tests.factories.user import UserFactory
from core.tests.factories.post import PostFactory
from core.models import Post


class OrganizationFilterTest(TestCase):
    def test_can_filter_by_username(self):
        post1 = PostFactory.create()
        post2 = PostFactory.create()
        post3 = PostFactory.create()

        user1 = UserFactory.create(username="user1")
        post1.created_by = user1
        post1.save()

        user2 = UserFactory.create(username="user2")
        post2.created_by = user2
        post2.save()

        post3.created_by = user2
        post3.save()

        qs = Post.objects.all()
        f = PostFilter(
            data={'username': 'user2'},
            queryset=qs,
        )
        self.assertEqual(f.qs.count(), 2)

        qs = Post.objects.all()

        f = PostFilter(
            data={'username': 'user1'},
            queryset=qs,
        )
        self.assertEqual(f.qs.count(), 1)
