# Generated by Django 4.0.1 on 2022-01-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_project_top_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='proj_img_1',
            field=models.ImageField(default='proj_default_img.png', upload_to='projects_images/subimgs'),
        ),
        migrations.AddField(
            model_name='project',
            name='yt_link',
            field=models.URLField(blank=True),
        ),
    ]
