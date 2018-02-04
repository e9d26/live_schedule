from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path(r'^$', views.schedule_list, name='schedule_list'),
]
