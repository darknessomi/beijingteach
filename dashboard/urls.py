from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^snippets/$', views.snippets, name='snippets'),
    url(r'^snippets/new/$', views.new_snippet, name='new_snippet'),
]
