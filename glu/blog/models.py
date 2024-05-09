from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.

class PostManager(models.Manager):
    def get_queryset(self) :
        return super().get_queryset().filter(status=Post.Status.PUBLISH)

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT="DR","Draft"
        PUBLISH="PB","Publish"

    tags=TaggableManager()
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog_post")
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(choices=Status.choices,default=Status.DRAFT,max_length=2)
    
    published=PostManager()
    objects=models.Manager()



    class Meta:
        ordering=['-publish']
        indexes=[models.Index(fields=['-publish'])]


    def get_absolute_url(self):
        return reverse("blog:post-detail",args=[self.publish.year,
         self.publish.month,self.publish.day,self.slug])

    def __str__(self) :
        return f"{self.title}"