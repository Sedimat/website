from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("single", views.single, name="single"),
    path("demo", views.demo, name="demo"),
    path("page", views.page, name="page"),
    path("blog", views.blog, name="blog"),
    path("archives", views.archives, name="archives"),
    path("my_form", views.my_form, name="my_form"),

]