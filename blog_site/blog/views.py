from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post

# Create your views here.
""" Function-based View of Post List
def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 5)
    curr_page = request.GET.get('page') # Used to retrieve the current page number
    
    try:
        posts = paginator.page(curr_page) # Would return the results of current page
    except PageNotAnInteger:
        posts = paginator.page(1) # Would return the first page of results
    except EmptyPage:
        posts = paginator.page(paginator.num_pages) # Would return the last page of results
    
    return render(request, 'blog/post/list.html', {'posts': posts, 'page': curr_page})
"""

# Class-based View of Post List
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'blog/post/list.html'

def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug = post,
        status = 'published',
        publish__year = year,
        publish__month = month,
        publish__day = day
    )
    return render(request, 'blog/post/detail.html', {'post': post})