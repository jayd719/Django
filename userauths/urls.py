from django.urls import path
from django.contrib.auth.views import LoginView
from userauths import views

urlpatterns = [
    path("sign-up/", views.user_register_view, name="sign-up"),
    path(
        "sign-in/",
        LoginView.as_view(template_name="userauths/signIn.html"),
        name="sign-in",
    ),
]
