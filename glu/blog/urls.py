from django.urls import path
from .views import Post_List,Detail_View


app_name="blog"

urlpatterns=[
    path('',Post_List.as_view(), name="post_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/", Detail_View.as_view(), name="post-detail")
]