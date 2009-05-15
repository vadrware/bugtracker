from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from bugtracker.core.models import *
from django.db.models import Q

@login_required
def index(request):
    return report01(request)
    
@login_required
def report01(request):
    #object_list = Defect.objects.complex_filter(Q(defectstate = u'O') | Q(defectstate = u'P') | Q(defectstate = u'V'));
    object_list = Defect.objects.filter(defectstate = u'O').order_by('productid__name', '-pk')
    return render_to_response('reports/report01.html', {'user': request.user, 'object_list': object_list})

@login_required
def report02(request):
    return render_to_response('reports/report02.html', {'user': request.user})    

class Report03Form(forms.Form):
    productversion = forms.ModelChoiceField(label='Select Product Version', queryset = ProductVersion.objects.all())

@login_required
def report03(request):
    if request.method == 'POST':
        object_list = Defect.objects.filter(projectversion__id = request.POST['productversion']).order_by('productid__name', '-pk')
        return render_to_response('reports/report03.html', {'user': request.user, 'object_list': object_list})
    else:
        form = Report03Form()
        return render_to_response('reports/report03_form.html', {'user': request.user, 'form': form})

@login_required
def report04(request):
    object_list = Defect.objects.filter(assigneddev = request.user).order_by('-id')
    return render_to_response('reports/report04.html', {'user': request.user, 'object_list': object_list})

@login_required
def report05(request):
    object_list = Defect.objects.filter(assignedqa = request.user).order_by('-id')
    return render_to_response('reports/report05.html', {'user': request.user, 'object_list': object_list})

@login_required
def report06(request):
    rs = Defect.objects.extra(select={'count': 'count(1)'}).values('defectstate', 'projectversion', 'productid', 'count')
    rs.query.group_by = ['defectstate', 'projectversion_id', 'productid_id']
    object_list = []
    for row in rs:
        version = ProductVersion.objects.get(id = row['projectversion'])
        product = Product.objects.get(id = row['productid'])
        object_list.append({'defectstate': Defect.defect_states_lookup[row['defectstate']], 'projectversion': version.version, 'productid': product.name, 'count': row['count']})
    return render_to_response('reports/report06.html', {'user': request.user, 'object_list': object_list})

#6.    Produce a count of bugs, for each state, sorted by product-version and product category.    

@login_required
def report07(request):
    object_list = Product.objects.all();
    return render_to_response('reports/report07.html', {'user': request.user, 'object_list': object_list})

@login_required
def report08(request):
    object_list = User.objects.all();
    return render_to_response('reports/report08.html', {'user': request.user, 'object_list': object_list})