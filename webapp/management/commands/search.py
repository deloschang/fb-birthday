from django.core.management.base import BaseCommand, CommandError
from webapp.models import *

import datetime  

class Command(BaseCommand):
    # must be named handle
    def handle(self, *args, **options):
        # process every date in the database
        # match date today
        self.stdout.write('Successful call')
