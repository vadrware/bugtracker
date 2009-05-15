import unittest
from models import *
from django.contrib.auth.models import User
from time import strftime

class productTestCase(unittest.TestCase):
	def setUp(self):
		self.p = Product.objects.create(name = 'awesome', description = 'a sweet product')

	def testStr(self):
		self.assertEquals(self.p.name,'awesome')
		self.assertEquals(self.p.description,'a sweet product')
		self.assertEquals(self.p.__str__(),'awesome')	

	def testGet_absolute_url(self):
		val = '/products/detail/'+str(self.p.pk)	
		self.assertEquals(self.p.get_absolute_url(),val)

class productversionTestCase(unittest.TestCase):
	def setUp(self):
		self.pv = ProductVersion.objects.create(version = '1.0',description = "the official release")

	def testStr(self):
		self.assertEquals(self.pv.__str__(),'1.0')

	def testGet_absolute_url(self):
		self.assertEquals(self.pv.get_absolute_url(),'/productversions/detail/'+str(self.pv.pk))

class resolutionTestCase(unittest.TestCase):
	def setUp(self):
		self.r = Resolution.objects.create(name = "fixed bug")
		self.r2 = Resolution.objects.create(name = "not a bug")

	def testStr(self):
		self.assertEquals(self.r.__str__(), "fixed bug")
		self.assertEquals(self.r2.__str__(), "not a bug")

	def testGet_absolute_url(self):
		val = '/resolutions/detail/'+str(self.r.pk)
		val2 = '/resolutions/detail/'+str(self.r2.pk)
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
		self.pr = Product.objects.create(name = 'awesome', description = "awwwright")
		self.re = Resolution.objects.create(name = "fixed bug")
		self.usr = User.objects.create_user('rich', 'rroslund@iit.edu', 'richpassword')
		self.prv = ProductVersion.objects.create(version = '1.0',description = "the official release")
		self.de = Defect.objects.create(productid = self.pr, projectversion=self.prv, postdate = strftime("%Y-%m-%d %H:%M:%S"), moddate = strftime("%Y-%m-%d %H:%M:%S"), defectstate = u'O',description = "bug description", reproduce = "do stuff, it breaks", resolutionid = self.re, userid = self.usr, modifieduserid = self.usr, assignedqa = self.usr, assigneddev = self.usr, assignedmgr = self.usr)
		de.save()
	
	def testStr(self):
		self.assertEquals(self.d.__str__(),self.de.pk)
	def testGet_absolute_url(self):
		self.assertEquals(self.d.__get_absolute_url(),'/defects/detail/1')
	def testDefect_states(self):
		self.assertEquals(self.d.defectstate,u'O')
		self.d.defectstate = u'P'
		self.assertEquals(self.d.defectstate,u'P')
		self.d.defectstate = u'V'
		self.assertEquals(self.d.defectstate,u'V')
		self.d.defectstate = u'C'
		self.assertEquals(self.d.defectstate,u'C')










