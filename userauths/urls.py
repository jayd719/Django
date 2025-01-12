from django.urls import path
from userauths import views

urlpatterns = [
    path("sign-up/", views.user_register_view, name="sign-up"),
    path("sign-in/", views.login_user_view, name="sign-in"),
    path("logout/", views.logout_user_view, name="logout"),
]
