from django.db import models
from core.models import *

# Create your models here.
class User (models.Model):
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
        removed = models.BooleanField()

class UserAccess (models.Model):
	userid = models.ForeignKey( User )
	userroleid = models.ForeignKey( UserRole )
	productid = models.ForeignKey( Product )

class DefectState (models.Model):
        defectCodes = (
                ( u'O', u'Open' ),
                ( u'P', u'Pending' ),
                ( u'V', u'Verifid' ),
                ( u'C', u'Closed' )
        )
        name = models.CharField( "Defect State", max_length = 50 )
        code = models.CharField( "Defect Code", max_length = 2, choices = defectCodes )

class Resolution (models.Model):
        name = models.CharField( "Resolution Name", max_length = 30 )

class Defect (models.Model):
	productid = models.ForeignKey( Product )
	projectversion = models.IntegerField()
	postdate = models.DateTimeField( "Post Date" )
	defectstatusid = models.ForeignKey( DefectState )
	reproduce = models.TextField()
	removed = models.BooleanField()
	resolutionid = models.ForeignKey( Resolution )
	userid = models.ForeignKey( User )

class Comment (models.Model):
	userid = models.ForeignKey( User )
	defectid = models.ForeignKey( Defect )
	postdate = models.DateTimeField( "Post Date" )
	description = models.TextField( "Comment Text" )
	removed = models.BooleanField()
	
class Duplicates (models.Model):
	originaldefectid = models.ForeignKey( Defect, related_name = "Original Defect" )
	duplicatedefectid = models.ForeignKey( Defect, related_name = "Duplicate Defect" )

