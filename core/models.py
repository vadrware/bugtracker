from django.db import models
from django import forms
from django.contrib.auth.models import User
from datetime import datetime
from time import strftime

# Create your models here.
class UserProfile (models.Model):
	userid = models.ForeignKey( User, unique = True )
	username = models.CharField( "Username", max_length = 50 )
	password = models.CharField( "Password", max_length = 50 )
	firstname = models.CharField( "First Name", max_length = 30 )
	lastname = models.CharField( "Last Name", max_length = 30 )
	active = models.BooleanField( "Active" ) 

class UserRole (models.Model):
	description = models.CharField( "Role Name", max_length = 50 )

class Product (models.Model):
    name = models.CharField( "Product Name", max_length = 100 )
    currentversion = models.IntegerField( "Current Product Version" )

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return "/%s/%s/%s" % ('products', 'detail', self.pk);

class UserAccess (models.Model):
	userid = models.ForeignKey( User )
	userroleid = models.ForeignKey( UserRole )
	productid = models.ForeignKey( Product )

class Resolution (models.Model):
    name = models.CharField( "Resolution", max_length = 30 )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return "/%s/%s/%s" % ('resolutions', 'detail', self.pk);

class Defect (models.Model):
    defect_states = (
                ( u'O', u'Open' ),
                ( u'P', u'Pending' ),
                ( u'V', u'Verifid' ),
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
        return "/defects"

#		return "/%s/%s/%s" % ('defects', 'detail', self.pk);

class Comment (models.Model):
	userid = models.ForeignKey( User )
	defectid = models.ForeignKey( Defect )
	postdate = models.DateTimeField( "Post Date" )
	description = models.TextField( "Comment Text" )
	
class Duplicates (models.Model):
	originaldefectid = models.ForeignKey( Defect, related_name = "Original Defect" )
	duplicatedefectid = models.ForeignKey( Defect, related_name = "Duplicate Defect" )

# ModelForm classes
class DefectForm(forms.ModelForm):
    postdate = forms.DateTimeField( required = False, widget = forms.HiddenInput() )
    moddate = forms.DateTimeField( required = False, widget = forms.HiddenInput() )

    class Meta:
        model = Defect


