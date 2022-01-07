from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
# from taggit.managers import TaggableManager
from django.urls import reverse
from PIL import Image

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from accounts.models import CustomUser

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    
    def __str__(self):
        return self.title


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    categories = models.ManyToManyField('Category', related_name='posts')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                               related_name='blog_posts')
    samplebody = models.TextField(max_length=100)
    body = RichTextUploadingField(blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    image = models.ImageField(default='defaul_article_img.png', upload_to='article_images')
    objects = models.Manager()
    published = PublishedManager()

    
    class Meta:
        ordering = ('-publish',)

    # admin show title instead of object
    def __str__(self):
        return self.title

    # absolute usl of post
    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'slug': self.slug} )

    
    # saving images to 600px
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=60)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return f'Commment by {self.name} on {self.post}'