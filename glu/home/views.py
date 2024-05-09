from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
from blog.models import Post


# Create your views here.

class Home(TemplateView):
    template_name="index.html"
    
    def get_context_data(self, **kwargs: Any) :
        context=super().get_context_data(**kwargs)
        context["data"]=Post.published.all()[0:3]

        return context
    