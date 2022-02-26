"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""Defines URL patterns for learning_logs."""
from django.urls import re_path , include
from . import views
urlpatterns = [
 re_path(r'^$', views.index, name='index'),
 
 # Show all topics.
 re_path(r'^topics/$', views.topics, name='topics'),
 
 #Show entry for individual topic
 re_path(r'^topics/(?P<topic_id>\d+)/$', views.entry, name='entry'),
 
 # Page for adding a new topic
 re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
 
 # Page for adding a new entry
 re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
 
 # Page for editing an entry
 re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
  ]
      
