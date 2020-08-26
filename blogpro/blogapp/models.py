from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# post related Model models here.
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')
from taggit.managers import TaggableManager
class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=264,unique_for_date='publish')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects=CustomManager()
    tags=TaggableManager()
    class Meta :
        ordering=('-publish',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        #return reverse('postdetails',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])
        return reverse('postdetails',args=[self.publish.year,self.publish.month,self.publish.day,self.slug])

#commentes related models
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=60)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    class Meta :
        ordering=('-created',)
    def __str__(self):
        return 'Commented by {} on {}'.format(self.name,self.post)
