from django.urls import path
from .views import Post_List


app_name="blog"

urlpatterns=[
    path('',Post_List.as_view(), name="post_list")
]