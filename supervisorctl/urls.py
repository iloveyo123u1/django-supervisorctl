from django.conf.urls import patterns, url

urlpatterns = patterns('supervisorctl.views',
    url(r'^$', 'index'),
    url(r'^service/$', 'service'),
)

