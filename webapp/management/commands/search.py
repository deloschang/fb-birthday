from django.core.management.base import BaseCommand, CommandError
from webapp.models import *

class Command(BaseCommand):
    # must be named handle
    def handle(self, *args, **options):
        self.stdout.write('Successful call')
