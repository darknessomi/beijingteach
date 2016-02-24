from django.conf.urls import include, url
from django.contrib import admin

from home import views as home

urlpatterns = [
    # plugin apps
    url(r'^x/', include(admin.site.urls)),
    url(r'^dashboard/', include('dashboard.urls', namespace='dashboard')),
]

urlpatterns += [
    # user pages (home app)
    url(r'^$', home.index, name='index'),
    url(r'^pages/(?P<slug>\w+)/$', home.customized_page, name='customized_page'),
    url(r'^contact/$', home.contact, name='contact'),
    url(r'^apply/$', home.apply, name='apply'),
]
