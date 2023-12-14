

from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("info", views.info, name="info"),
    path("hw1", views.hw1, name="hw1"),

]