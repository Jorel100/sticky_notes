from django.test import TestCase
from .models import BulletinPost
from django.urls import reverse


class BulletinPostTest(TestCase):

    def setUp(self):
        self.post = BulletinPost.objects.create(title='Test Post', content='This is a test post.')

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.content, 'This is a test post.')

    def test_post_list_view(self):
        response = self.client.get(reverse('bulletin_post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        response = self.client.get(reverse('bulletin_post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is a test post')

# Create your tests here.
