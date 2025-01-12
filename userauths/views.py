from django.shortcuts import render, redirect, HttpResponse
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

app_name = "userauths"

LOGIN_FAILED_MESSAGE = '<div class="border border-red-500 bg-red-100 text-red-600 p-3 rounded-lg h-auto grid">Oops! Your email or password is incorrect. Remember, passwords are case-sensitive. Try again! <br><a class="link-primary" href="/reset-password/">Forgot password?</a></div>'
ENABLE_COOKIE_MESSAGE = '<div class="border border-red-500 bg-red-100 text-red-600 p-3 rounded-lg h-auto grid">Please enable cookies and try again.</div>'


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
            firstname = form.cleaned_data.get("first_name")

            # Flash success message
            messages.success(
                request, f"Hey {firstname}!, Your Account was created successfully"
            )

            # Authenticate user--> username is replace by email as primary identifier
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


def login_user_view(request):
    """
    Handles user login.

    - If the request method is POST, it validates the email and password.
    - If authentication is successful, the user is logged in and redirected to the homepage.
    - If authentication fails, an error message is displayed and the user is redirected to the login page.
    - If the request method is GET, the login page is displayed.

    Returns:
        - Renders the login template for GET requests.
        - Redirects the user to the homepage after successful login.
        - Redirects the user back to the login page with an error message on failure.
    """
    if request.method == "POST":
        email = request.POST.get("id_email_login")
        password = request.POST.get("id_password_login")

        # if request.session.test_cookie_worked():
        #     request.session.delete_test_cookie()
        #     return HttpResponse(ENABLE_COOKIE_MESSAGE)

        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return HttpResponse("<script>location.reload()</script>")
        else:
            return HttpResponse(LOGIN_FAILED_MESSAGE)


def logout_user_view(request):
    logout(request)
    messages.success(request, "User logged out successfully.")
    return redirect("home")
