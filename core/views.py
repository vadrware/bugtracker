# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response

class AuthenticationController (object):

	def __call__( self, request, action ):
		if( not len(action) ):
			action = 'index'

		return getattr(self, action)( request )
		
	def index( self, request ):
		return self.login( request )

	def login( self, request ):
		return render_to_response('login.html')
