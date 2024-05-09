from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Post

# Create your views here.


class Post_List(ListView):
    template_name="posts/posts.html"
    context_object_name="posts"
    queryset=Post.published.all()

class Detail_View(DetailView):
    template_name="posts/detail.html"
    context_object_name="post"
    
    def get_object(self, queryset=None):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        post_slug = self.kwargs.get('post')
        
        return get_object_or_404(
            Post,
            slug=post_slug,
            publish__year=year,
            publish__month=month,
            publish__day=day,
            status=Post.Status.PUBLISH
        )