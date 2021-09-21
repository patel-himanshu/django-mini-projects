from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.


class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@gmail.com",
            password="somesecret"
        )

        self.post = Post.objects.create(
            title="A test blog",
            author=self.user,
            body="Some gibberish test content for the blog"
        )

    def test_string_representation(self):
        post = Post(title="A test blog")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "A test blog")
        self.assertEqual(f"{self.post.author}", "testuser")
        self.assertEqual(f"{self.post.body}",
                         "Some gibberish test content for the blog")

    def test_post_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, "Some gibberish test content for the blog")
        self.assertTemplateUsed(response, "home.html")

    def test_post_detail_view(self):
        response = self.client.get("/post/1/")
        no_response = self.client.get("/post/100/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A test blog")
        self.assertContains(
            response, "Some gibberish test content for the blog")
        self.assertTemplateUsed(response, "post_detail.html")

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'title': "New Blog Title",
            "author": self.user.id,
            'body': "Some content for the test blog"
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New Blog Title")
        self.assertEqual(Post.objects.last().body,
                         "Some content for the test blog")

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': "Updated title",
            'body': "Updated body"
        })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 302)
