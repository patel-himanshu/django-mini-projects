from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Article

# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'author', 'body')
    template_name = 'article_new.html'


class ArticleEditView(UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'article_edit.html'


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
