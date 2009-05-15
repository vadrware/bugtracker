import unittest
from models import *
from django.contrib.auth.models import User
from time import strftime

class productTestCase(unittest.TestCase):
	def setUp(self):
		self.usr = User.objects.create_user('rich3', 'rroslund@iit.edu', 'richpassword')
		self.p = Product.objects.create(name = 'awesome3', description = 'a sweet product', assignedqa=self.usr,assigneddev=self.usr,assignedmgr=self.usr)

	def testStr(self):
		self.assertEquals(self.p.name,'awesome3')
		self.assertEquals(self.p.description,'a sweet product')
		self.assertEquals(self.p.__str__(),'awesome3')	

class product2TestCase(unittest.TestCase):
	def setUp(self):
		self.usr1 = User.objects.create_user('rich1', 'rroslund@iit.edu', 'richpassword')
		self.p1 = Product.objects.create(name = 'awesome1', description = 'a sweet product', assignedqa=self.usr1,assigneddev=self.usr1,assignedmgr=self.usr1)

	def testGet_absolute_url(self):
		val = '/products/detail/'+str(self.p1.pk)	
		self.assertEquals(self.p1.get_absolute_url(),val)

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

	def testStr(self):
		self.assertEquals(self.r.__str__(), "fixed bug")

	def testGet_absolute_url(self):
		val = '/resolutions/detail/'+str(self.r.pk)
		self.assertEquals(self.r.get_absolute_url(),val)


class userprofileTestCase(unittest.TestCase):
	def setUp(self):
		self.user = User.objects.create_user('adam', 'akadzban@iit.edu', 'adampassword')
		self.up = UserProfile.objects.create(userid=self.user,active=1)

	def testStr(self):
		self.assertEquals(self.up.__str__(),'adam')

class defectTestCase(unittest.TestCase):
	def setUp(self):
		self.user = User.objects.create_user('rich', 'rroslund@iit.edu', 'richpassword')
		self.p = Product.objects.create(name = 'awesome', description = "awwwright",assignedqa=self.user,assigneddev=self.user,assignedmgr=self.user)
		self.r = Resolution.objects.create(name = "fixed bug")
		self.pv = ProductVersion.objects.create(version = '1.0',description = "the official release")
		self.d = Defect.objects.create(productid = self.p, projectversion=self.pv, postdate = strftime("%Y-%m-%d %H:%M:%S"), moddate = strftime("%Y-%m-%d %H:%M:%S"), defectstate = u'O',description = "bug description", reproduce = "do stuff, it breaks", resolutionid = self.r, userid = self.user, modifieduserid = self.user, assignedqa = self.user, assigneddev = self.user, assignedmgr = self.user)
		self.d.save()

	def testStr(self):
		self.assertEquals(self.d.__str__(),self.d.pk)

class defect2TestCase(unittest.TestCase):
	def setUp(self):
		self.usr = User.objects.create_user('rich2', 'rroslund@iit.edu', 'richpassword')
		self.pr = Product.objects.create(name = 'awesome2', description = "awwwright",assignedqa=self.usr,assigneddev=self.usr,assignedmgr=self.usr)
		self.re = Resolution.objects.create(name = "fixed bug2")
		self.prv = ProductVersion.objects.create(version = '1.1',description = "the official release")
		self.de = Defect.objects.create(productid = self.pr, projectversion=self.prv, postdate = strftime("%Y-%m-%d %H:%M:%S"), moddate = strftime("%Y-%m-%d %H:%M:%S"), defectstate = u'O',description = "bug description", reproduce = "do stuff, it breaks", resolutionid = self.re, userid = self.usr, modifieduserid = self.usr, assignedqa = self.usr, assigneddev = self.usr, assignedmgr = self.usr)
		self.de.save()

	def testGet_absolute_url(self):
		self.assertEquals(self.de.get_absolute_url(),'/defects/detail/'+str(self.de.pk))
