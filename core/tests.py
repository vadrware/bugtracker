import unittest
from models import *
from django.contrib.auth.models import User

class productTestCase(unittest.TestCase):
	def setUp(self):
		self.p = Product.objects.create(name = 'awesome', currentversion = 1)

	def testStr(self):
		self.assertEquals(self.p.name,'awesome')
		self.assertEquals(self.p.currentversion, 1)
		self.assertEquals(self.p.__str__(),'awesome')	

	def testGet_absolute_url(self):
		val = '/products/detail/1'	# p will be first bug, id will be 1?  maybe		
		self.assertEquals(self.p.get_absolute_url(),val)

class resolutionTestCase(unittest.TestCase):
	def setUp(self):
		self.r = Resolution.objects.create(name = "fixed bug")
		self.r2 = Resolution.objects.create(name = "not a bug")

	def testStr(self):
		self.assertEquals(self.r.__str__(), "fixed bug")
		self.assertEquals(self.r2.__str__(), "not a bug")

	def testGet_absolute_url(self):
		val = '/resolutions/detail/1'
		val2 = '/resolutions/detail/2'
		self.assertEquals(self.r.get_absolute_url(), val)
		self.assertEquals(self.r2.get_absolute_url(), val2)


class userprofileTestCase(unittest.TestCase):
	def setUp(self):
		self.user = User.objects.create_user('adam', 'akadzban@iit.edu', 'adampassword')
		self.up = UserProfile.objects.create(userid=self.user,active=1)

	def testStr(self):
		print(self.up.__str__())
		self.assertEquals(self.up.__str__(),'adam')
		self.assertEquals(self.up.active,1)

class defectTestCase(unittest.TestCase):
	def setUp(self):
		self.p = Product.objects.create(name = 'awesome', currentversion = 1)
		self.r = Resolution.objects.create(name = "fixed bug")
		self.user = User.objects.create_user('adam', 'akadzban@iit.edu', 'adampassword')
		self.d = Defect.objects.create(productid = self.p, productversion=1.5)

#	def 
