from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
<<<<<<< HEAD
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
=======
    author = models.ForeignKey(User, related_name='blog_posts')
>>>>>>> 259a420113a376c4c94a5bedd2a8a7520e486b45
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title