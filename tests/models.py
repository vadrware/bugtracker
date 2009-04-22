from django.db import models

# Create your models here.
class Testdefect(models.Model):
	field1 = models.CharField( max_length = 1000 )
	field2 = models.IntegerField()

class Testuser(models.Model):
	username = models.CharField( max_length = 50 )
	password = models.CharField( max_length = 50 )
	email = models.CharField( max_length = 400 )
