from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.


class Post_List(ListView):
    template_name="posts/posts.html"
    context_object_name="posts"
    queryset=Post.published.all()
