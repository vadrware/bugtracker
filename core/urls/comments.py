from django.conf.urls.defaults import *
from bugtracker.core.models import *

urlpatterns = patterns('',
    (r'^/$', 'django.views.generic.list_detail.object_list', 
        dict(queryset = Comment.objects.all(), paginate_by = 30)),
    (r'^/detail/(?P<object_id>\d+)/?$', 'django.views.generic.list_detail.object_detail', 
        dict(queryset = Comment.objects.all())),
    (r'^/create/?$', 'django.views.generic.create_update.create_object', 
        dict(model = Comment)),
    (r'^/update/(?P<object_id>\d+)/?$', 'django.views.generic.create_update.update_object', 
        dict(model = Comment)),
    (r'^/delete/(?P<object_id>\d+)/?$', 'django.views.generic.create_update.delete_object', 
        dict(model = Comment, post_delete_redirect = "..")),
)
