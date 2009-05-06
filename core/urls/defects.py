from django.conf.urls.defaults import *
from bugtracker.core.models import *

urlpatterns = patterns('',
    (r'^/$', 'django.views.generic.list_detail.object_list', 
        dict(queryset = Defect.objects.all(), paginate_by = 30)),
    (r'^/detail/(?P<object_id>\d+)/?$', 'django.views.generic.list_detail.object_detail', 
        dict(queryset = Defect.objects.all())),
    (r'^/create/?$', 'django.views.generic.create_update.create_object', 
        dict(model = Defect, form_class = DefectForm, login_required = True)),
    (r'^/update/(?P<object_id>\d+)/?$', 'django.views.generic.create_update.update_object', 
        dict(model = Defect, form_class = DefectForm, login_required = True)),
    (r'^/delete/(?P<object_id>\d+)/?$', 'django.views.generic.create_update.delete_object', 
        dict(model = Defect, login_required = True, post_delete_redirect = "/defects")),
)
