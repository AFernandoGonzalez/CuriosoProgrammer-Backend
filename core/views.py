from django.shortcuts import render

from .models import Project, AboutMe, Skill, Education, Certificate, WorkingOn, ReadingListening

def home_view(request):
    return render(request, 'core/home.html')

def about_view(request):
    about_me = AboutMe.objects.all()
    skills = Skill.objects.all()
    educations = Education.objects.all()
    certificates = Certificate.objects.all()
    context = {
        'about_me': about_me,
        'skills': skills,
        'educations': educations,
        'certificates': certificates
    }
    return render(request, 'core/about.html', context)

def portfolio_view(request):
    return render(request, 'core/portfolio.html')

def portfolio_detail_view(request):
    return render(request, 'core/portfolio_detail.html')

def contact_view(request):
    return render(request, 'core/contact.html')


