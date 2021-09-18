from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="This is sample text 1")
        Post.objects.create(text="This is sample text 2")
        Post.objects.create(text="This is sample text 3")

    def test_text_content(self):
        post = Post.objects.get(id=2)
        post_text_content = f"{post.text}"
        self.assertEqual(post_text_content, "This is sample text 2")


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text="Another set of text for testing")

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
