from django.core.management.base import BaseCommand
from home.models import SnippetPos


class Command(BaseCommand):

    snippet_pos_init_data = [
        {'slug': 'about'},
        {'slug': 'experience'},
        {'slug': 'china'},
        {'slug': 'accommodations'},
    ]

    def handle(self, *args, **options):
        for d in self.snippet_pos_init_data:
            print 'Update or create SnippetPos(%s)' % d
            SnippetPos.objects.update_or_create(**d)
