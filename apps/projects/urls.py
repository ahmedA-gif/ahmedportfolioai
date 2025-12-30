from django.urls import path
from . import views

urlpatterns=[
    path('',views.project_list,name='project_list'),
    path('api/',views.api_projects,name='api_projects'),
    path("projects/<path:slug>/", views.project_detail, name="project_detail"),

]