from django.contrib import admin
from userauths.models import User


class UserAdminView(admin.ModelAdmin):
    list_display = ["username", "email", "first_name", "last_name"]


admin.site.register(User, UserAdminView)

# Register your models here.
