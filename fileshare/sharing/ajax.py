from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from dajaxice.core import dajaxice_functions
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
@dajaxice_register
def sayhello(request,text):
	try:
		a=User.objects.get(username=text).username
		pass
	except ObjectDoesNotExist:
		a=None
	return simplejson.dumps({'message':a})
	# return simplejson.dumps({'message':'ss'})
dajaxice_functions.register(sayhello)
