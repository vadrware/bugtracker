from django.conf.urls.defaults import *
from bugtracker.core.views import *
from bugtracker.core.models import *
from django.conf import settings
from django.contrib.comments.models import Comment
from bugtracker.core.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^bugtracker/', include('bugtracker.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),

    # static content
    (r'^app_media/(?P<path>.*)$', 'django.views.static.serve',
	{'document_root': settings.STATIC_DOC_ROOT}),

    # authentication
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),

    # comments
    (r'^comments/', include('django.contrib.comments.urls')),

    # bugtracker core
    (r'^defects', include('bugtracker.core.urls.defects')),
    (r'^products', include('bugtracker.core.urls.products')),
    (r'^resolutions', include('bugtracker.core.urls.resolutions')),
    (r'^accounts', include('bugtracker.core.urls.accounts')),

    (r'^$', login_required(object_list), 
        dict(queryset = Defect.objects.all(), paginate_by = 20)),
)
