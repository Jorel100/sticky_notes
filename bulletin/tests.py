from django.test import TestCase
from .models import BulletinPost
from django.urls import reverse


class BulletinPostTest(TestCase):

    def setUp(self):
        self.post = BulletinPost.objects.create(
            title='Test Post',
            content='This is a test post.'
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.content, 'This is a test post.')
        self.assertIsNotNone(self.post.created_at)
        self.assertIsNotNone(self.post.updated_at)
