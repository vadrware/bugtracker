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
		self.pr = Product.objects.create(name = 'awesome', description = "awwwright")
		self.re = Resolution.objects.create(name = "fixed bug")
		self.usr = User.objects.create_user('rich', 'rroslund@iit.edu', 'richpassword')
		self.prv = ProductVersion.objects.create(version = '1.0',description = "the official release")
		self.de = Defect.objects.create(productid = self.pr, projectversion=self.prv, postdate = strftime("%Y-%m-%d %H:%M:%S"), moddate = strftime("%Y-%m-%d %H:%M:%S"), defectstate = u'O',description = "bug description", reproduce = "do stuff, it breaks", resolutionid = self.re, userid = self.usr, modifieduserid = self.usr, assignedqa = self.usr, assigneddev = self.usr, assignedmgr = self.usr)
		self.de.save()

	def testUsr(self):
		self.assertEquals(self.usr.username,'rich')
		self.assertEquals(self.usr.email,'rroslund@iit.edu')

#	def testStr(self):
#		self.assertEquals(self.de.__str__(),self.de.pk)
#	def testGet_absolute_url(self):
#		self.assertEquals(self.de.get_absolute_url(),'/defects/detail/'+str(self.de.pk))
'''	def testDefect_states(self):
		self.assertEquals(self.de.defectstate,u'O')
		self.de.change_state(u'P')
		self.assertEquals(self.de.defectstate,u'P')
		self.de.change_state(u'V')
		self.assertEquals(self.de.defectstate,u'V')
		self.de.change_state(u'C')
		self.assertEquals(self.de.defectstate,u'C')
		self.de.change_state(u'B')
		self.assertNotEquals(self.de.defectstate,u'B')
'''












