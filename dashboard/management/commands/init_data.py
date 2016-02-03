from django.core.management.base import BaseCommand
from dashboard.models import SnippetPos, PagePos, SiteSetting


class Command(BaseCommand):

    snippet_pos_init_data = [
        {'slug': 'about'},
        {'slug': 'experience'},
        {'slug': 'china'},
        {'slug': 'accommodations'},
    ]

    page_pos_init_data = [
        {'slug': 'about'},
        {'slug': 'experience'},
        {'slug': 'china'},
        {'slug': 'accommodations'},
    ]

    site_setting_init_data = [
        {
            'key': 'header_links',
            'defaults': {
                'value': '|'.join(d['slug'] for d in page_pos_init_data)
            },
        },
    ]

    def add_arguments(self, parser):
        parser.add_argument('--with-templates',
                            action='store_true',
                            dest='with_templates',
                            default=False,
                            help='Create default templates.')

    def handle(self, *args, **options):

        for d in self.snippet_pos_init_data:
            print 'Update or create SnippetPos(%s)' % d
            SnippetPos.objects.update_or_create(**d)

        for d in self.page_pos_init_data:
            print 'Update or create PagePos(%s)' % d
            PagePos.objects.update_or_create(**d)

        for d in self.site_setting_init_data:
            print 'Update or create SiteSetting(%s)' % d
            SiteSetting.objects.update_or_create(**d)

        if options['with_templates']:
            self.auto_templates()

        print 'All Done!\nMay your system never fail!'

    def auto_templates(self):
        print 'Create default templates...'
