from django.urls import reverse_lazy
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from .models import Post

class LatestPostsFeed(Feed):
    title = 'My Blog'
    link = reverse_lazy('blog:post_list')
    description = 'My new blog posts'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)