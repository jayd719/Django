from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={"placeholder": "First Name"})
    )

    last_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={"placeholder": "Last Name"})
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
