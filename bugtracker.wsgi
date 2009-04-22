import os
import sys
sys.path.append('/var/www/vadrware')
os.environ['PYTHON_EGG_CACHE'] = '/tmp/bugtracker/python-eggs'
os.environ['DJANGO_SETTINGS_MODULE'] = 'bugtracker.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
