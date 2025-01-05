from django.shortcuts import render
from userauths.forms import UserRegisterForm

app_name = "userauths"


def user_register_view(request):
    form = UserRegisterForm()
    context = {"form": form}
    return render(request, "userauths/signup.html", context)
