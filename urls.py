from django.conf.urls.defaults import *
from bugtracker.core.views import *
from bugtracker.core.models import *
from django.conf import settings
from django.contrib.comments.models import Comment
from bugtracker.core.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import *
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

    # authentication and account management
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    (r'^accounts/password_reset/$', 'django.contrib.auth.views.password_reset'),
    (r'^accounts/password_reset_done/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^accounts/password_reset_confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^accounts/password_reset_complete/$', 'django.contrib.auth.views.password_reset_complete'),

    # comments
    (r'^comments/', include('django.contrib.comments.urls')),

    # bugtracker core
    (r'^defects', include('bugtracker.core.urls.defects')),
    (r'^products', include('bugtracker.core.urls.products')),
    (r'^productversions', include('bugtracker.core.urls.productversions')),
    (r'^resolutions', include('bugtracker.core.urls.resolutions')),
    (r'^accounts', include('bugtracker.core.urls.accounts')),
    
    # reports
    (r'^reports/$', 'bugtracker.core.reports.index'),
    (r'^reports/report01', 'bugtracker.core.reports.report01'),
    (r'^reports/report02', 'bugtracker.core.reports.report02'),
    (r'^reports/report03', 'bugtracker.core.reports.report03'),
    (r'^reports/report04', 'bugtracker.core.reports.report04'),
    (r'^reports/report05', 'bugtracker.core.reports.report05'),
    (r'^reports/report06', 'bugtracker.core.reports.report06'),
    (r'^reports/report07', 'bugtracker.core.reports.report07'),
    (r'^reports/report08', 'bugtracker.core.reports.report08'),

    (r'^$', login_required(object_list), 
        dict(queryset = Defect.objects.all(), paginate_by = 20)),
)
