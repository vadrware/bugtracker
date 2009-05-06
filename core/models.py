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
        return "/%s/%s/%s" % ('products', 'detail', self.pk);

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
        return "/%s/%s/%s" % ('resolutions', 'detail', self.pk);

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
    defectstate = models.CharField( "Defect State", max_length = 1, choices = defect_states )
    reproduce = models.TextField( "Steps to Reproduce" )
    resolutionid = models.ForeignKey( Resolution, verbose_name = "Resolution" )
    userid = models.ForeignKey( User, verbose_name = "Created By" )

    def save(self):
        if self.postdate == None:
            self.postdate = strftime("%Y-%m-%d %H:%M:%S")
        self.moddate = strftime("%Y-%m-%d %H:%M:%S")
        super(Defect, self).save()

	def __str__(self):
		return self.pk

    def get_absolute_url(self):
        return "/%s/%s/%s" % ('defects', 'detail', self.pk);
	
# duplicates model, links defect with other related defects
# currently not used
class Duplicates (models.Model):
	originaldefectid = models.ForeignKey( Defect, related_name = "Original Defect" )
	duplicatedefectid = models.ForeignKey( Defect, related_name = "Duplicate Defect" )

#
# ModelForm classes
#

# customize how defect forms render
class DefectForm(forms.ModelForm):
    postdate = forms.DateTimeField( required = False, widget = forms.HiddenInput() )
    moddate = forms.DateTimeField( required = False, widget = forms.HiddenInput() )

    class Meta:
        model = Defect


