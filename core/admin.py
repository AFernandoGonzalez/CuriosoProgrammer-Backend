from django.contrib import admin

from .models import AboutMe, Skill, Education, Certificate, Project, ReadingListening

# Register your models here.
admin.site.register(AboutMe)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Certificate)
admin.site.register(Project)
admin.site.register(ReadingListening)