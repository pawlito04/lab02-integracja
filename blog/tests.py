from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_post_string_representation(self):
        post = Post.objects.create(
            title='Testowy wpis',
            content='To jest treść testowego wpisu.',
            author=self.user,
            published_at=timezone.now()
        )
        self.assertEqual(str(post), 'Testowy wpis')


class PostViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.post = Post.objects.create(
            title='Widoczny wpis',
            content='Treść wpisu',
            author=self.user,
            published_at=timezone.now()
        )

    def test_post_list_view_status_code(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 404)

    def test_post_list_view_uses_correct_template(self):
        response = self.client.get('/blog/')
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_post_detail_view_status_code(self):
        response = self.client.get(f'/blog/post/{self.post.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view_uses_correct_template(self):
        response = self.client.get(f'/blog/post/{self.post.pk}/')
        self.assertTemplateUsed(response, 'blog/post_detail.html')
