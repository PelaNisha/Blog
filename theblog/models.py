from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    bio =models.TextField()

    def __str__(self):
        return str(self.user)

class post(models.Model):
    title = models.CharField(max_length = 255)
    header_image = models.ImageField(null = True, blank = True, upload_to = 'image/')
    title_tag = models.CharField(max_length=255, default='New post')
    Category= models.CharField(max_length=255, default='Coding')
    author = models.ForeignKey(User, on_delete =models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    body = RichTextField(blank =True, null = True)
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name = 'blog_posts')
    snippet= models.CharField(max_length=255)

    def total_likes(self):
        return self.likes.count()


    def __str__(self):
        return self.title+ "|" + str(self.author)


    def get_absolute_url(self):
        return reverse('article_details', args=(str(self.id)))    
