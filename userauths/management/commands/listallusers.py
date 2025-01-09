"""-------------------------------------------------------
Django: Custom Command
----------------------------------------------------------
Author:  JD
ID:      91786
Uses:    
Version:  1.0.8
__updated__ = Thu Jan 05 2025
-------------------------------------------------------"""

from userauths.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Custom Django management command to print a list of all users."""

    help = "Prints a list of all users in the database."

    def handle(self, *args, **options):
        users = User.objects.all()
        user_count = users.count()

        if user_count == 0:
            self.stdout.write(self.style.WARNING("No users found."))
            return

        self.stdout.write(self.style.SUCCESS(f"{user_count} Users Found"))
        for user in users:
            self.stdout.write(
                f"- {user.first_name} {user.last_name} (ID: {user.id}, Email: {user.email})"
            )
