from django.http import HttpResponse
from django.views.generic.create_update import *
from django.views.generic.list_detail import *
from bugtracker.core.models import Defect, DefectForm
from django import forms

def create(request):

    # pass current authenticated user to django form
    if request.method == 'POST':
        request.POST = request.POST.copy()
        request.POST.appendlist('user', '%d' % (request.user.id))
        request.POST.appendlist('userid', '%d' % (request.user.id))
        request.POST.appendlist('modifieduserid', '%d' % (request.user.id))
       
    return create_object(request, Defect, form_class = DefectForm, login_required = True)

def update(request, object_id):

    # pass current authenticated user to django form
    if request.method == 'POST':
        request.POST = request.POST.copy()
        request.POST.appendlist('user', '%d' % (request.user.id))
        request.POST.appendlist('modifieduserid', '%d' % (request.user.id))
       
    return update_object(request, Defect, form_class = DefectForm, login_required = True, object_id = object_id)
