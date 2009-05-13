from django.db import models
from django import forms
from django.contrib.auth.models import User
from time import strftime

#
# application core models
#

# additional variables associated with user, this links up with django.contrib.auth.models.User
class UserProfile (models.Model):
	userid = models.ForeignKey( User, unique = True )
	firstname = models.CharField( "First Name", max_length = 30 )
	lastname = models.CharField( "Last Name", max_length = 30 )
	active = models.BooleanField( "Active" ) 

# product model
class Product (models.Model):
    name = models.CharField( "Product Name", max_length = 100 )
    currentversion = models.IntegerField( "Current Product Version" )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/%s/%s/%s" % ('products', 'detail', self.pk)

# useraccess model, ties users to products to configure which users have access to mess with tickets for which products
# currently not used
class UserAccess (models.Model):
	userid = models.ForeignKey( User )
	productid = models.ForeignKey( Product )

# defect resolution model
class Resolution (models.Model):
    name = models.CharField( "Resolution", max_length = 30 )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/%s/%s/%s" % ('resolutions', 'detail', self.pk)

# defect model
class Defect (models.Model):
    defect_states = (
                ( u'O', u'Open' ),
                ( u'P', u'Pending' ),
                ( u'V', u'Verified' ),
                ( u'C', u'Closed' )
        )
    productid = models.ForeignKey( Product, verbose_name = "Product" )
    projectversion = models.IntegerField( "Product Version" )
    postdate = models.DateTimeField( "Post Date", blank = True )
    moddate = models.DateTimeField( "Modified Date", blank = True )
    defectstate = models.CharField( "Defect State", max_length = 1, choices = defect_states, default = u'O' )
    description = models.TextField( "Short Description" )
    reproduce = models.TextField( "Steps to Reproduce" )
    resolutionid = models.ForeignKey( Resolution, verbose_name = "Resolution" )
    userid = models.ForeignKey( User, verbose_name = "Created By", related_name = "Created By" )
    assignedqa = models.ForeignKey( User, verbose_name = "Assigned QA", related_name = "Assigned QA" )
    assigneddev = models.ForeignKey( User, verbose_name = "Assigned Developer", related_name = "Assigned Developer" )

    def save(self):
        if self.postdate == None:
            self.postdate = strftime("%Y-%m-%d %H:%M:%S")
        self.moddate = strftime("%Y-%m-%d %H:%M:%S")
        super(Defect, self).save()

	def __str__(self):
		return self.pk

    def get_absolute_url(self):
        return "/%s/%s/%s" % ('defects', 'detail', self.pk)
	
#
# ModelForm classes
#

# customize how defect forms render
class DefectForm(forms.ModelForm):
    postdate = forms.DateTimeField( required = False, widget = forms.HiddenInput() )
    moddate = forms.DateTimeField( required = False, widget = forms.HiddenInput() )
    user = forms.IntegerField( required = False, widget = forms.HiddenInput() )
    userid = forms.ModelChoiceField( required = False, widget = forms.HiddenInput(), queryset = User.objects.all() )
    					   
    class Meta:
        model = Defect

    def __init__(self, *args, **kwargs):
        super(DefectForm, self).__init__(*args, **kwargs)
        # filter selection lists to appropriate group members
        self.fields["assignedqa"].queryset = User.objects.filter(groups__name = 'QA')
        self.fields["assigneddev"].queryset = User.objects.filter(groups__name = 'Developers')
        
    def clean_defectstate(self): 
    	
    	# make sure new defects start in open state   
    	if self.cleaned_data.get('defectstate') != u'O' and self.instance.pk == u'None':
            raise forms.ValidationError('New defects must start in Open state.')
           
        if self.instance.pk == u'None' or (self.instance.pk != u'None' and self.cleaned_data.get('defectstate') == self.instance.defectstate):
           return self.cleaned_data.get('defectstate')

    	user = User.objects.get( id = self.data.get('user') )

        # only pending defects can be verified
        if self.cleaned_data.get('defectstate') == u'V' and self.instance.defectstate != u'P':
        	raise forms.ValidationError('Defects must be in pending state before they can be verified.')

        # only verified defects can be closed
        if self.cleaned_data.get('defectstate') == u'C' and self.instance.defectstate != u'V':
        	raise forms.ValidationError('Defects must be verified before they can be closed.')
                      
        # make sure only users in managers group can close defects in verified state
        if self.cleaned_data.get('defectstate') == u'C' and user.groups.filter(name = 'Managers').count() == 0:
        	raise forms.ValidationError('Only managers can close verified defects.')
                
        # only assigned qa person may change defect state from pending to verified
        if self.cleaned_data.get('defectstate') == u'V' and self.instance.defectstate == u'P' and int(user.id) != int(self.data.get('assignedqa')):
        	raise forms.ValidationError('Only assigned QA person may change state to verified.')                
                
        return self.cleaned_data.get('defectstate')


