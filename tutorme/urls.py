from django.contrib import admin
from django.urls import include, path

from . import views


app_name = 'tutorme'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('accounts/', include('allauth.urls')),
    path('auth/', views.AuthView.as_view(), name='auth'),
    path('student/', views.StudentView.as_view(), name='student'),
    path('student/schedule/', include('schedule_builder.urls')),

    path('student/<username>', views.profile, name='profile'),
    
    path('search/', views.SearchForTutor.as_view(), name='searchForTutor'),
    path('addClasses/', views.TutorAddClassView.as_view(), name='tutorAddClasses'),
    path('about/', views.AboutView.as_view(), name='about'),
    # path('requests/', views.all_requests, name='requests'),
]
