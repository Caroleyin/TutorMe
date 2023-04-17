from django.contrib import admin
from django.urls import include, path

from schedule_builder import views

app_name = 'schedule_builder'
urlpatterns = [
    path('', views.index, name='schedule_index'), 
    path('all_events/', views.all_events, name='all_events'), 
    path('add_event/', views.add_event, name='add_event'), 
    path('update/', views.update, name='update'),
    path('remove/', views.remove, name='remove'),
    #path('tutor/', views.profile, name='tutor'),
    path('tutor/<username>', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='tutorme/index.html'), name='logout')
]