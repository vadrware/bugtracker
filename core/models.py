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
	active = models.BooleanField( "Active" ) 
	
	def __str__(self):
		return self.userid.username

# product model
class Product (models.Model):
    name = models.CharField( "Product Category Name", max_length = 100 )
    description = models.TextField( "Description", blank = True )
    assignedqa = models.ForeignKey( User, verbose_name = "Assigned QA", related_name = "Category Assigned QA" )
    assigneddev = models.ForeignKey( User, verbose_name = "Assigned Developer", related_name = "Category Assigned Developer" )
    assignedmgr = models.ForeignKey( User, verbose_name = "Assigned Manager", related_name = "Category Assigned Manager" )
        
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return "/%s/%s/%s" % ('products', 'detail', self.pk)

class ProductVersion (models.Model):
    version = models.CharField( "Version", max_length = 30 )
    description = models.TextField( "Description", blank = True )

    def __str__(self):
        return self.version
    def get_absolute_url(self):
        return "/%s/%s/%s" % ('productversions', 'detail', self.pk)

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
    defect_states_lookup = {u'O': u'Open', u'P': u'Pending', u'V': u'Verified', u'C': u'Closed'}
    
    productid = models.ForeignKey( Product, verbose_name = "Product Category" )
    projectversion = models.ForeignKey( ProductVersion, verbose_name = "Product Version" )
    postdate = models.DateTimeField( "Post Date", blank = True )
    moddate = models.DateTimeField( "Modified Date", blank = True )
    defectstate = models.CharField( "Defect State", max_length = 1, choices = defect_states, default = u'O' )
    description = models.TextField( "Short Description" )
    reproduce = models.TextField( "Steps to Reproduce", blank = True )
    resolutionid = models.ForeignKey( Resolution, verbose_name = "Resolution" )
    userid = models.ForeignKey( User, verbose_name = "Created By", related_name = "Created By" )
    modifieduserid = models.ForeignKey( User, verbose_name = "Modified By", related_name = "Modified By" )
    assignedqa = models.ForeignKey( User, verbose_name = "Assigned QA", related_name = "Assigned QA" )
    assigneddev = models.ForeignKey( User, verbose_name = "Assigned Developer", related_name = "Assigned Developer" )
    assignedmgr = models.ForeignKey( User, verbose_name = "Assigned Manager", related_name = "Assigned Manager" )

    def save(self,*args, **kwargs):
        if self.postdate == None:
            self.postdate = strftime("%Y-%m-%d %H:%M:%S")
        self.moddate = strftime("%Y-%m-%d %H:%M:%S")
        super(Defect, self).save(*args, **kwargs)
    def __str__(self):
        return self.pk
    def get_absolute_url(self):
        return "/%s/%s/%s" % ('defects', 'detail', self.pk)
'''
when this gets called, it errors: "AttributeError: 'Defect' object has no attribute 'change_state'".  lolwut?
	def change_state(self, newstate):
		if newstate in defect_states:
			self.state=newstate
'''	
#
# ModelForm classes
#

# customize how defect forms render
class DefectForm (forms.ModelForm):
    postdate = forms.DateTimeField( required = False, widget = forms.HiddenInput() )
    moddate = forms.DateTimeField( required = False, widget = forms.HiddenInput() )
    user = forms.IntegerField( required = False, widget = forms.HiddenInput() )
    userid = forms.ModelChoiceField( required = False, widget = forms.HiddenInput(), queryset = User.objects.all() )
    modifieduserid = forms.ModelChoiceField( required = False, widget = forms.HiddenInput(), queryset = User.objects.all() )
    assignedqa = forms.ModelChoiceField( label = 'Assigned QA', queryset = User.objects.filter(groups__name = 'QA') )
    assigneddev = forms.ModelChoiceField( label = 'Assigned Developer', queryset = User.objects.filter(groups__name = 'Developers') )
    assignedmgr = forms.ModelChoiceField( label = 'Assigned Manager', queryset = User.objects.filter(groups__name = 'Managers') )
	    					   
    class Meta:
        model = Defect

    def clean_defectstate(self): 
        # make sure new defects start in open state     
        if str(self.cleaned_data.get('defectstate')) != u'O' and str(self.instance.pk) == u'None':
            raise forms.ValidationError('New defects must start in Open state.')
        if str(self.instance.pk) == u'None' or (str(self.instance.pk) != u'None' and str(self.cleaned_data.get('defectstate')) == str(self.instance.defectstate)):
           return self.cleaned_data.get('defectstate')

    	user = User.objects.get( id = self.data.get('user') )

        # only pending defects can be verified
        if str(self.cleaned_data.get('defectstate')) == u'V' and str(self.instance.defectstate) != u'P':
        	raise forms.ValidationError('Defects must be in pending state before they can be verified.')
        # only verified defects can be closed
        if str(self.cleaned_data.get('defectstate')) == u'C' and str(self.instance.defectstate) != u'V':
        	raise forms.ValidationError('Defects must be verified before they can be closed.')
        # make sure only users in managers group can close defects in verified state (and only the assigned manager)
        if str(self.cleaned_data.get('defectstate')) == u'C' and (user.groups.filter(name = 'Managers').count() == 0 or int(user.id) != int(self.data.get('assignedmgr'))):
        	raise forms.ValidationError('Only assigned manager can close verified defect.')
        # only assigned qa person may change defect state from pending to verified
        if str(self.cleaned_data.get('defectstate')) == u'V' and str(self.instance.defectstate) == u'P' and int(user.id) != int(self.data.get('assignedqa')):
        	raise forms.ValidationError('Only assigned QA person may change state to verified.')                

        return self.cleaned_data.get('defectstate')

class ProductForm (forms.ModelForm):
	assignedqa = forms.ModelChoiceField( label = 'Assigned QA', queryset = User.objects.filter(groups__name = 'QA') )
	assigneddev = forms.ModelChoiceField( label = 'Assigned Developer', queryset = User.objects.filter(groups__name = 'Developers') )
	assignedmgr = forms.ModelChoiceField( label = 'Assigned Manager', queryset = User.objects.filter(groups__name = 'Managers') )
	
	class Meta:
		model = Product


