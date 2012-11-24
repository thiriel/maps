from django.conf.urls.defaults import *
from django.contrib.auth.forms import AuthenticationForm

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('helpme.views',
        (r'^$','helpme'),
        (r'^alert','alert'),
    )
