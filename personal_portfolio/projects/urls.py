from django.urls import path

from . import views

urlpatterns = [

    path('', views.show_display),
    path('', views.projects_detail),
]

