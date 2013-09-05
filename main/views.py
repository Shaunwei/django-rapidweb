from django.shortcuts import render_to_response
from django.template import RequestContext
from payments.models import User

def index(request):
	uid = request.session.get('user')
	if uid is None:
		return render_to_response('index.html',
					{'user':[]},
					context_instance = RequestContext(request))
	else:
		return render_to_response('user.html',
					{'user':User.objects.get(pk=uid)},
					context_instance = RequestContext(request))

	
