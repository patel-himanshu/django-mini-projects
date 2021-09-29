from django.contrib.auth.models import User
from django.test import TestCase

from .models import Post

# Create your tests here.


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create(
            username='testuser', password='abcd1234'
        )
        test_user.save()

        test_post = Post.objects.create(
            author=test_user, title='Test title', body='Test body'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser')
        self.assertEqual(title, 'Test title')
        self.assertEqual(body, 'Test body')
