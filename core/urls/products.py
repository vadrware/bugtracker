from django.conf.urls.defaults import *
from bugtracker.core.models import Product, ProductForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import *

urlpatterns = patterns('',
    (r'^/$', login_required(object_list), 
        dict(queryset = Product.objects.all(), paginate_by = 20)),
    (r'^/detail/(?P<object_id>\d+)/?$', login_required(object_detail), 
        dict(queryset = Product.objects.all())),
    (r'^/create/?$', 'django.views.generic.create_update.create_object', 
        dict(model = Product, form_class = ProductForm, login_required = True)),
    (r'^/update/(?P<object_id>\d+)/?$', 'django.views.generic.create_update.update_object', 
        dict(model = Product, form_class = ProductForm, login_required = True)),
    (r'^/delete/(?P<object_id>\d+)/?$', 'django.views.generic.create_update.delete_object', 
        dict(model = Product, login_required = True, post_delete_redirect = "/products")),
)
