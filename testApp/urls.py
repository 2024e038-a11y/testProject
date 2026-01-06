from django.urls import path
from . import views

urlpatterns = [
    path("", views.timeline, name='timeline'),
    path("new/", views.post_new, name='post_new'),
]