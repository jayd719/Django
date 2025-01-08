from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from userauths import views

urlpatterns = [
    path("sign-up/", views.user_register_view, name="sign-up"),
    path("sign-in/", views.login_user_view, name="sign-in"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
