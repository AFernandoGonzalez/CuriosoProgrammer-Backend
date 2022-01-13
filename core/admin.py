from django.contrib import admin

from .models import  AboutMe, Skill, WorkingOn , Education, Certificate, Project, ReadingListening, Contact

# Register your models here.
admin.site.register(AboutMe)
admin.site.register(Skill)
admin.site.register(WorkingOn)
admin.site.register(Education)
admin.site.register(Certificate)
admin.site.register(Project)
admin.site.register(ReadingListening)
admin.site.register(Contact)