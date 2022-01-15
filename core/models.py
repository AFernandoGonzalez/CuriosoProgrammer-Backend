from django.db import models
from PIL import Image
from ckeditor.fields import RichTextField

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email

class Project(models.Model):
    proj_title = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=100)
    long_desc = RichTextField(blank=True, null=True)
    tech_used = models.CharField(max_length=20)
    proj_url = models.URLField(max_length=200, blank=True)
    blog_link = models.URLField(max_length=200, blank=True)
    proj_img = models.ImageField(default='proj_default_img.png', upload_to='projects_images')
    top_project = models.BooleanField(default=False)

    class Meta:
        ordering = ('-proj_title',)

    def __str__(self):
        return self.proj_title

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.proj_img.path)
    #     if img.height > 600 or img.width > 600:
    #         output_size = (700, 700)
    #         img.thumbnail(output_size)
    #         img.save(self.proj_img.path)


class AboutMe(models.Model):
    my_img = models.ImageField(default='aboutme_default_img.png', upload_to='aboutme_images')
    name = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=500)
    email = models.EmailField(max_length=100)
    instagram_link = models.URLField(max_length=200, blank=True)
    linkedIn_link = models.URLField(max_length=200, blank=True)
    facebook_link = models.URLField(max_length=200, blank=True)
    youtube_link = models.URLField(max_length=200, blank=True)


    def __str__(self):
        return self.name


class Skill(models.Model):
    tech_title = models.CharField(max_length=50)

    def __str__(self):
        return self.tech_title


class Education(models.Model):
    college_name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)

    def __str__(self):
        return self.college_name


class Certificate(models.Model):
    certificate_name = models.CharField(max_length=100)
    certificate_issued = models.CharField(max_length=100)

    def __str__(self):
        return self.certificate_name

class WorkingOn(models.Model):
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class ReadingListening(models.Model):
    bookname = models.CharField(max_length=200, blank=True)
    audioname = models.CharField(max_length=200, blank=True)

    def __str__(self):
        # return self.certificate_name
        return f'Reading {self.bookname} and listening {self.audioname}'