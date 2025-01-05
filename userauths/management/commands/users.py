from userauths.models import User
from django.core.management import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Prints list of all users"

    def handle(self, *args, **options):
        users = User.objects.all()
        print(f"{len(users)} Users Found")
        for user in users:
            print(user)
