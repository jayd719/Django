from django.urls import path
from userauths import views

urlpatterns = [
    path("sign-up", views.user_register_view, name="sign-up"),
]
