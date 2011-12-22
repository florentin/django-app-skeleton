from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = 'Does stuff.'
    def handle_noargs(self, **options):
        pass
