from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('application/', views.application_view, name='applicantion'),
    path('resumeupload/', views.resume_upload, name='resume'),
]
