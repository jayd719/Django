from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

app_name = "userauths"


def user_register_view(request):
    """
    Handles user registration.

    - If the request method is POST, it validates and processes the registration form.
    - On successful registration, the user is logged in and redirected to a dashboard/home page.
    - If the form is invalid, errors are displayed.
    - If the request method is GET, an empty registration form is displayed.

    Returns:
        - Renders the signup template with the form.
        - Redirects the user to the homepage/dashboard after successful registration.
    """
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")

            # Flash success message
            messages.success(
                request, f"Hey {username}!, Your Account was created successfully"
            )

            # Authenticate user
            authenticated_user = authenticate(
                username=form.cleaned_data.get("email"),
                password=form.cleaned_data.get("password1"),
            )
            # Log the user in automatically after registration
            login(request, authenticated_user)

            return redirect("home")
    else:
        form = UserRegisterForm()

    context = {"form": form}
    return render(request, "userauths/signup.html", context)
