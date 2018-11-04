from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.post_list, name='post_list'),
]