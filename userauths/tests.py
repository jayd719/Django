from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from userauths.forms import UserRegisterForm

User = get_user_model()


class UserRegisterViewTests(TestCase):
    """Tests for the user registration view."""

    @classmethod
    def setUpTestData(cls):
        """Set up initial data that is shared across tests."""
        cls.register_url = reverse("userauths:register")
        cls.home_url = reverse("home")

        cls.valid_user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password1": "TestPass123!",
            "password2": "TestPass123!",
        }

        cls.invalid_user_data = {
            "username": "",
            "email": "invalidemail",
            "password1": "short",
            "password2": "mismatch",
        }

    def test_get_register_page(self):
        """Test that GET request loads the signup page successfully."""
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "userauths/signup.html")
        self.assertIsInstance(response.context["form"], UserRegisterForm)

    def test_successful_registration(self):
        """Test successful user registration and login."""
        response = self.client.post(
            self.register_url, self.valid_user_data, follow=True
        )

        # Ensure user is created
        self.assertTrue(User.objects.filter(username="testuser").exists())

        # Ensure user is logged in
        user = response.context["user"]
        self.assertTrue(user.is_authenticated)
        self.assertEqual(user.username, "testuser")

        # Ensure redirection to home page
        self.assertRedirects(response, self.home_url)

        # Ensure success message appears
        messages = [str(msg) for msg in get_messages(response.wsgi_request)]
        self.assertIn("Account created successfully! Welcome, testuser!", messages)

    def test_registration_fails_invalid_data(self):
        """Test that invalid form submission does not create a user."""
        response = self.client.post(self.register_url, self.invalid_user_data)

        # Ensure user was NOT created
        self.assertFalse(User.objects.filter(email="invalidemail").exists())

        # Ensure form errors are displayed
        self.assertFormError(response, "form", "username", "This field is required.")
        self.assertFormError(response, "form", "email", "Enter a valid email address.")
        self.assertFormError(
            response, "form", "password2", "The two password fields didn’t match."
        )

        # Ensure the same page is re-rendered
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "userauths/signup.html")

    def test_duplicate_user_registration(self):
        """Test that registering with an existing email fails."""
        # Create initial user
        User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="TestPass123!",
        )

        response = self.client.post(self.register_url, self.valid_user_data)

        # Ensure duplicate user is not created
        self.assertEqual(User.objects.filter(email="testuser@example.com").count(), 1)

        # Ensure an error message is shown
        self.assertFormError(
            response, "form", "email", "User with this Email already exists."
        )

        # Ensure page is re-rendered
        self.assertEqual(response.status_code, 200)

    def test_password_validation(self):
        """Test that weak passwords fail registration."""
        weak_password_data = {
            "username": "weakuser",
            "email": "weakuser@example.com",
            "password1": "123",
            "password2": "123",
        }

        response = self.client.post(self.register_url, weak_password_data)

        # Ensure user is not created
        self.assertFalse(User.objects.filter(email="weakuser@example.com").exists())

        # Ensure error message is displayed
        self.assertFormError(
            response,
            "form",
            "password1",
            "This password is too short. It must contain at least 8 characters.",
        )

        # Ensure page is re-rendered
        self.assertEqual(response.status_code, 200)

    def test_registration_fails_authentication(self):
        """Test case where user creation succeeds, but authentication fails."""
        # Simulate incorrect authentication by modifying password before login attempt
        self.valid_user_data["password1"] = "WrongPass"

        response = self.client.post(
            self.register_url, self.valid_user_data, follow=True
        )

        # Ensure user is created but authentication fails
        self.assertTrue(User.objects.filter(username="testuser").exists())

        user = response.context["user"]
        self.assertFalse(user.is_authenticated)  # Should not be logged in

        # Check error message
        messages = [str(msg) for msg in get_messages(response.wsgi_request)]
        self.assertIn("Authentication failed. Please log in manually.", messages)
