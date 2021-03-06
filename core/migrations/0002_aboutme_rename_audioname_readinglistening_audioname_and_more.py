# Generated by Django 4.0.1 on 2022-01-07 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_img', models.ImageField(default='aboutme_default_img.png', upload_to='aboutme_images')),
                ('name', models.CharField(max_length=100)),
                ('short_desc', models.CharField(max_length=500)),
                ('instagram_link', models.URLField(blank=True)),
                ('linkedIn_link', models.URLField(blank=True)),
                ('facebook_link', models.URLField(blank=True)),
                ('youtube_link', models.URLField(blank=True)),
            ],
        ),
        migrations.RenameField(
            model_name='readinglistening',
            old_name='AudioName',
            new_name='audioname',
        ),
        migrations.RenameField(
            model_name='readinglistening',
            old_name='BookName',
            new_name='bookname',
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='title',
            new_name='tech_title',
        ),
        migrations.RenameField(
            model_name='workingon',
            old_name='Name',
            new_name='name',
        ),
    ]
