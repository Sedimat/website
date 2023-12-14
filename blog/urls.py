from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<str:id>", views.post, name="post"),
    path("category/<str:name>", views.category, name="category"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("about/", views.about, name="about"),
    path("login", LoginView.as_view(), name='blog_login'),
    path("logout", views.logout_view, name='logout'),
    path("user", views.user, name='user'),
    path("delete_post/<int:post_id>/", views.delete_post, name="delete_post"),
    path("edit_user/<int:user_id>/", views.edit_user, name="edit_user")

]

# path("logout", LogoutView.as_view(), name='blog_logout'),