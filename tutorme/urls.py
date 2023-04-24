from django.contrib import admin
from django.urls import include, path

from . import views


app_name = 'tutorme'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('accounts/', include('allauth.urls')),
    path('auth/', views.AuthView.as_view(), name='auth'),
    path('landing/', views.StudentView.as_view(), name='landing'),
    path('student/schedule/', include('schedule_builder.urls')),

    path('student/<username>', views.profile, name='profile'),
    
    path('search/', views.SearchForTutor.as_view(), name='searchForTutor'),

    path('about/', views.AboutView.as_view(), name='about'),
    path('requests/', views.all_requests, name='requests'),
]
