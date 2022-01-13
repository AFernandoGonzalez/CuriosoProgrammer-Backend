from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('portfolio/<int:pk>', views.portfolio_detail_view, name='portfolio-detail'),
    path('contact/', views.contact_view, name='contact'),
    
]