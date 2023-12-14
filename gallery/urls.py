from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.gallery, name="gallery"),
    path('uploads/', views.upload, name='upload')
]