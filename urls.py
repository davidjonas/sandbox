from django.conf.urls import *

urlpatterns = patterns('sandbox.views',
    url(r'^$', 'home'),
    url(r'^api/(?P<func>\S*)', 'api'),
    url(r'', 'redirect_to_home')
)
    