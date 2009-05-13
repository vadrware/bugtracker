from django.conf.urls.defaults import *
from bugtracker.core.models import *
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import *

urlpatterns = patterns('',
    (r'^/$', login_required(object_list), 
        dict(queryset = Defect.objects.all(), paginate_by = 20)),
    (r'^/detail/(?P<object_id>\d+)/?$', login_required(object_detail), 
        dict(queryset = Defect.objects.all())),
    (r'^/create/?$', 'bugtracker.core.defects.create'),
    (r'^/update/(?P<object_id>\d+)/?$', 'bugtracker.core.defects.update'),
    (r'^/delete/(?P<object_id>\d+)/?$', 'django.views.generic.create_update.delete_object', 
        dict(model = Defect, login_required = True, post_delete_redirect = "/defects")),
)
