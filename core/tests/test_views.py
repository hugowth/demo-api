import os
from rest_framework.test import APITestCase
from django.urls import reverse

from core.models import User
from core.tests.factories.user import UserFactory
from core.tests.factories.post import PostFactory


class UserRegistrationViewTest(APITestCase):

    create_view = 'public:user-register-list'

    def test_can_register_user(self):
        response = self.client.post(
            reverse(self.create_view),
            data={'username': 'test', 'password': 'test'},
        )
        self.assertEqual(response.status_code, 201)

    def test_cant_register_user(self):
        UserFactory.create(username='test')

        response = self.client.post(
            reverse(self.create_view),
            data={'username': 'test', 'password': 'test'},
        )
        self.assertEqual(response.status_code, 400)


class TokenObtainPairViewTest(APITestCase):
    login_view = 'public:token_obtain_pair'

    def test_can_login_user(self):
        user = User.objects.create(username='test')
        user.set_password('test')
        user.save()

        response = self.client.post(
            reverse(self.login_view),
            data={'username': 'test', 'password': 'test'},
        )
        self.assertEqual(response.status_code, 200)

    def test_cant_login_user(self):
        user = User.objects.create(username='test')
        user.set_password('test')
        user.save()

        response = self.client.post(
            reverse(self.login_view),
            data={'username': 'test', 'password': 'xx'},
        )

        self.assertEqual(response.status_code, 401)


class PostViewSetTest(APITestCase):
    post_view = 'public:post-list'

    @classmethod
    def setUpTestData(cls):
        cls.customer = UserFactory.create()

    def test_can_create_post(self):
        self.client.force_authenticate(self.customer)

        file = os.path.join(
            os.path.dirname(__file__),
            './test.jpg',
        )

        with open(file, 'rb') as f:
            response = self.client.post(
                reverse(self.post_view),
                data={'image': f, 'description': 'description'},
                format='multipart',

            )

        self.assertEqual(response.status_code, 201)

    def test_can_list_post(self):
        self.client.force_authenticate(self.customer)

        post1 = PostFactory.create()
        post2 = PostFactory.create()
        post3 = PostFactory.create()

        response = self.client.get(reverse(self.post_view))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 3)
