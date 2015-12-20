from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.index, name='index'),
    url(r'^snippets/$',
        views.snippets, name='snippets'),
    url(r'^snippets/new/$',
        views.new_snippet, name='new_snippet'),
    url(r'^snippets/(?P<snippet_id>\d+)/$',
        views.update_snippet, name='update_snippet'),
]
