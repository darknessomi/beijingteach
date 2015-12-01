from django.conf.urls import include, url
from django.contrib import admin

from home import views as home
from dashboard import views as dashboard

urlpatterns = [
    # plugin apps
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += [
    # user pages (home app)
    url(r'^$', home.index, name='index'),
    url(r'^about/$', home.about, name='about'),
    url(r'^experience/$', home.experience, name='experience'),
    url(r'^china/$', home.china, name='china'),
    url(r'^accommodations/$', home.accommodations, name='accommodations'),
    url(r'^contact/$', home.contact, name='contact'),
    url(r'^apply/$', home.contact, name='apply'),
]

urlpatterns += [
    # dashboard pages (dashboard app)
    url(r'^dashboard/$', dashboard.index),
]
