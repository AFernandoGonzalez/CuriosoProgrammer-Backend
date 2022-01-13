from django.conf import settings
from django.core.mail import send_mail

from django.shortcuts import render

from blog.models import Category, Post

from django.core.paginator import Paginator

from .models import Project, AboutMe, Skill, Education, Certificate, WorkingOn, ReadingListening

from .forms import ContactForm


def home_view(request):
    project = Project.objects.all()[:5]
    posts = Post.objects.all()[:4]

    context = {
        'project': project,
        'posts': posts,
    }
    return render(request, 'core/home.html', context)

def about_view(request):
    about_me = AboutMe.objects.all()
    skills = Skill.objects.all()
    workingOn = WorkingOn.objects.all()
    readlisten = ReadingListening.objects.all()
    educations = Education.objects.all()
    certificates = Certificate.objects.all()
    context = {
        'about_me': about_me,
        'skills': skills,
        'workingOn': workingOn,
        'readlisten': readlisten,
        'educations': educations,
        'certificates': certificates
    }
    return render(request, 'core/about.html', context)

def portfolio_view(request):
    top_project = Project.objects.filter(top_project=True)
    project = Project.objects.filter(top_project=False)

    paginator = Paginator(project, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'project': project,
        'top_project': top_project,
        'page_obj': page_obj,
    }
    return render(request, 'core/portfolio.html', context)

def portfolio_detail_view(request, pk):
    project = Project.objects.get(pk=pk)

    context = {
        'project': project,
    }
    return render(request, 'core/portfolio_detail.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            return render(request, 'core/email_success.html')

    form = ContactForm()
    context = {
        'form': form
        }
    return render(request, 'core/contact.html', context)


