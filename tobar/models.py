from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from map.models import Well


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=100)
    well = models.ForeignKey(
        Well, on_delete=models.CASCADE, related_name='wells', default='1')
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tobar_posts')
    featured_image = CloudinaryField('image', default='placeholder')
    cures = models.CharField(
        max_length=100, default='autofilled on save', blank=True)
    location = models.CharField(
        max_length=100, default='autofilled on save', blank=True)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='tobarpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
