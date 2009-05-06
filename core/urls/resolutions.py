from django.conf.urls.defaults import *
from bugtracker.core.models import *
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import *

urlpatterns = patterns('',
    (r'^/$', login_required(object_list), 
        dict(queryset = Resolution.objects.all(), paginate_by = 30)),
    (r'^/detail/(?P<object_id>\d+)/?$', login_required(object_detail), 
        dict(queryset = Resolution.objects.all())),
    (r'^/create/?$', 'django.views.generic.create_update.create_object', 
        dict(model = Resolution, login_required = True)),
    (r'^/update/(?P<object_id>\d+)/?$', 'django.views.generic.create_update.update_object', 
        dict(model = Resolution, login_required = True)),
    (r'^/delete/(?P<object_id>\d+)/?$', 'django.views.generic.create_update.delete_object', 
        dict(model = Resolution, login_required = True, post_delete_redirect = "/resolutions")),
)
