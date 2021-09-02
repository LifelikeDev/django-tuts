from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("counter", views.counter, name="counter"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("post_home", views.post_home, name="post_home"),
    path("post/<str:post_route>", views.post, name="post")
]
