from django.shortcuts import render

app_name = "userauths"


def user_register_view(request):
    return render(request, "usersauths/signup.html")
