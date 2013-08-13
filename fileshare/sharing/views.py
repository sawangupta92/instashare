# a=subprocess.Popen(('find'), stdout=subprocess.PIPE)
# >>> o=subprocess.check_output(('grep','man'),stdin=a.stdout)
# cd /home/sawan/Desktop/instashare| find -name PRIVATE -exec grep -R -Hn import {} \;
from django.core.files.base import ContentFile
from django.core.files import File
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.contrib.auth import logout
from django.contrib.auth.models import User
import json
from django.db.models import Q
from django.shortcuts import render_to_response,redirect,HttpResponse	
from sharing.models import *
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib.auth.decorators import login_required
from sharing.models import *
from django.template import RequestContext
from django.db import IntegrityError
from subprocess import CalledProcessError
from rauth import OAuth1Service
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist 
from django.core.files.uploadedfile import SimpleUploadedFile
import os
twitter = OAuth1Service(
    consumer_key='qXmrGK3UflaHcLYD8IUpBQ',
    consumer_secret='cobN4a9Nu4rh8Rr6i3NV3AXHIVBUYl2i31PpE7fg24',
    name='twitter',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authorize',
    request_token_url='https://api.twitter.com/oauth/request_token',
    base_url='https://api.twitter.com/1/')
TWITTER_CONSUMER_KEY = 'qXmrGK3UflaHcLYD8IUpBQ'
TWITTER_CONSUMER_SECRET_KEY = 'cobN4a9Nu4rh8Rr6i3NV3AXHIVBUYl2i31PpE7fg24'
FACEBOOK_APP_ID = '156809224510615'
FACEBOOK_SECRET_KEY = '3612fc5bb9416cf6e22b1894aef68b32'
FACEBOOK_REQUEST_PERMISSIONS = ''
# django.contrib.auth.context_processors.auth
############################################DECORATORS#########################################
class employee_already_associated_with_company(object):
	def __init__(self, orig_func):
		self.orig_func = orig_func
	def __call__(self, request, *args, **kwargs):
		a=employee.objects.get(employee_id=User.objects.get(username=request.user))
		if a.company_id==None:
			return render_to_response('company_template/view_of_create_company.html')
		else:
			return self.orig_func(request, *args, **kwargs)
class admin_decorator_required(object):
	def __init__(self, orig_func):
		self.orig_func = orig_func
	def __call__(self, request, *args, **kwargs):
		r_emp=roles_emp.objects.get(u_id=request.user.id)
		if roles.objects.get(id=r_emp.roles_id_id).role_name=='super admin' or roles.objects.get(id=r_emp.roles_id_id).role_name=='admin':
			return self.orig_func(request, *args, **kwargs)
		else:
			return render_to_response('index/admin_decorator_required_fail.html')

####################################VIEW OF EMPLOYEE###########################################

# @admin_decorator_required
def view_of_create_employee(request):#admin decorator logout
	all_objects=roles.objects.filter()
	return render_to_response('employee_template/view_of_create_employee.html',{'a':all_objects})
	pass
@csrf_exempt
@admin_decorator_required
def create_employee(request):#admin decorator logout
	u=User.objects.create_user(username=request.POST.get('name'),password=request.POST.get('password'),email=request.POST.get('email_id'),first_name=request.POST.get('f_name'),last_name=request.POST.get('l_name'))
	u_c=User.objects.get(username=request.user)
	c=company.objects.get(company_id=u_c)
	e=employee.objects.create(employee_id=u,company_id=c,address=request.POST.get('address') ,phone_no=request.POST.get('phone'),fb_id=request.POST.get('fb_id'), twitter_id=request.POST.get('tw_id'))
	r_id=roles.objects.get(role_name=request.POST.get('role','tester'))
	r=roles_emp.objects.create(roles_id=r_id,u_id=u)
	e.save()
	r.save()
	return render_to_response('employee_template/create_employee.html')
	pass
# @admin_decorator_required
def view_of_delete_employee(request):#logout add admin decorator
	all_objects=employee.objects.filter()
	return render_to_response('employee_template/view_of_delete_employee.html',{'a':all_objects})
@csrf_exempt
@admin_decorator_required
def delete_employee(request):#admin decorator logout
	u=User.objects.get(username=request.POST.get('employee_name'))
	a=employee.objects.get(employee_id=u)
	a.delete()
	return render_to_response('employee_template/delete_employee.html')
def view_of_update_employee(request,name):
	employee_object=employee()
	employee_fields=employee_object.fields_of_employee()
	return render_to_response('employee_template/view_of_update_employee.html',{'fields':employee_fields,'name':name})	
	pass
@csrf_exempt
def employee_save_update(request):
	a=employee.objects.get(employee_id=User.objects.get(username=request.POST.get('employee_name')))
	setattr(a,request.POST.get('field'),request.POST.get('update'))
	a.save()
	return render_to_response('employee_template/employee_save_update.html',{'a':a})

###################################### VIEW OF COMPANY################################################
@employee_already_associated_with_company
def view_of_create_company(request):#admin decorator logout
	return render_to_response('company_template/view_of_create_company.html')
@csrf_exempt
@admin_decorator_required
def create_company(request):#admin decorator logout
	u=User.objects.create_user(username=request.POST.get('name'),password=request.POST.get('password'),email=request.POST.get('email_id'))
	c=company.objects.create(company_id=u,address=request.POST.get('address') ,phone_no=request.POST.get('phone'), website=request.POST.get('website'), fb_id=request.POST.get('fb_id'), twitter_id=request.POST.get('twitter_id'))
	a=employee.objects.get(employee_id=User.objects.get(username=request.user))
	a.company_id=c
	c.save()
	a.save()
	return render_to_response('company_template/create_company.html')
# @admin_decorator_required
def view_of_delete_company(request):#logout add admin login decorator
	all_objects=company.objects.filter()
	return render_to_response('company_template/view_of_delete_company.html',{'a':all_objects})
@csrf_exempt
@login_required
@admin_decorator_required
def delete_company(request):#login also redirect to login page and logout the current user
	# u=User.objects.get(username=request.user)
	# u=User.objects.get(username=request.POST.get('company_name'))
	e=employee.objects.get(employee_id=User.objects.get(username=request.user))
	a=company.objects.get(id=e.company_id_id)
	a.delete()
	return render_to_response('index/index.html')
def view_of_update_company(request):
	company_object=company()
	company_fields=company_object.fields_of_company()
	return render_to_response('company_template/view_of_update_company.html',{'fields':company_fields})
@admin_decorator_required
def company_save_update(request):
	a=company.objects.get(company_id=User.objects.get(username=request.user))
	setattr(a,request.GET.get('field','w'),request.GET.get('update','w'))
	a.save()
	return render_to_response('company_template/company_save_update.html')
def company_operations(request):
	all_objects=roles.objects.filter()
	# emp=employee.objects.get(employee_id=User.objects.get(username=request.user))
	# emps=company.objects.get(employee=User.objects.get(username=request.user)).employee_set.filter()
	e=employee.objects.get(employee_id=User.objects.get(username=request.user))
	emps=company.objects.get(employee=e).employee_set.filter()
	return render_to_response('company_template/company.html',{'emps':emps,'a':all_objects},context_instance=RequestContext(request))
	pass

#########################################VIEW OF FILE##############################################
def show_file(request):
	# import mimetypes
	# import os
	# mimetypes.init()
	# file_path="/home/sawan/Desktop/instashare/readme.txt"
	fsock=open("/home/sawan/Desktop/instashare/readme.txt","rb")
	f=fsock.readlines()
	# file_name=os.path.basename(file_path)
	# mime_type_guess=mimetypes.guess_type(file_name)
	# response = HttpResponse(fsock, mimetype=mime_type_guess[0])
	# response['Content-Disposition'] = 'attachment; filename=' + file_name
	return render_to_response('file/show_file.html',{'f':f})
	pass
@login_required
def view_of_upload_file(request):#logout index delete_file view_my_file view_company_file*
	return render_to_response('file/view_of_upload_file.html')
@csrf_exempt
@login_required
def upload_file(request):#logout index delete_file view_my_file view_company_file* add_another_file 
	try:
		form=file_upload(request.POST, request.FILES)
		user=User.objects.get(username=request.user)
		emp=employee.objects.get(employee_id=user)
		a=request.FILES['document']
		t = ExtFileField(ext_whitelist=(".py", ".txt"))
		t.clean(SimpleUploadedFile(a.name,'Some File Content'))
		instance=my_file.objects.create(file_to_upload=request.FILES['document'],employee_who_added_file=emp, file_name=request.FILES['document'], access=request.POST.get('access','PUBLIC'))
		return redirect(index)
		pass
	except ValidationError, e:
		return render_to_response('index/test.html')
@login_required
def view_of_my_file(request):#logout index delete_file view_company_file* add_file
	a=User.objects.get(username=request.user)
	e=employee.objects.get(employee_id=a.id)
	f=my_file.objects.filter(employee_who_added_file=e)
	return render_to_response('file/view_of_my_file.html',{'files':f})
	pass
def view_my_company_file(request):#logout index delete_file view_my_file add_file
	a=User.objects.get(username=request.user)
	e=employee.objects.get(employee_id=a.id)
	c=company.objects.get(id=e.company_id_id)
	emps=employee.objects.filter(company_id=c)
	files=my_file.objects.filter(Q(employee_who_added_file__in=emps)&Q(access='COMPANY'))
	# files=my_file.objects.filter(Q(access='COMPANY')|Q(access='PUBLIC'))
	pages=Paginator(files,10)
	return render_to_response('file/view_my_company_file.html',{'name':files, 'pages':pages.object_list, 'p':list(files)},context_instance=RequestContext(request))
	pass
def view_of_delete_file(request):#logout index  view_my_file view_company_file* add_file
	a=User.objects.get(username=request.user)
	e=employee.objects.get(employee_id=a.id)
	f=my_file.objects.filter(employee_who_added_file=e)
	return render_to_response('file/view_of_delete_file.html',{'files':f})
	pass
@csrf_exempt
def delete_my_file(request):#logout index delete_file view_my_file view_company_file* add_file
	myfile=request.POST.get('file_to_delete')
	f=my_file.objects.get(file_to_upload=myfile)
	f.file_to_upload.delete()
	f.delete()
	return redirect(index)
	# return render_to_response('file/delete_my_file.html',{'file':myfile})
	pass
def file_access_validator(request,access,a):
	if access=='PUBLIC':
		return True
		pass
	elif access=='COMPANY':
		if employee.objects.get(employee_id=User.objects.get(username=request.user)).company_id_id==employee.objects.get(id=a.employee_who_added_file_id).company_id_id:
			return True
		else:
			return False
	else:
		if employee.objects.get(employee_id=User.objects.get(username=request.user))==employee.objects.get(id=a.employee_who_added_file_id):
			return True
		else:
			return False
	pass
# sabse pehle file ka access check kar if public no problem if company check kar ki jo user h vo usi company ka h ya nhi else private ke liye dekh ki file ussi user ne upload kri h naa
def wysiwyg_editor(request, path): 
	# -- check which file.
	# if()
	full_file=my_file.objects.get(id=path)
	val=file_access_validator(request,full_file.access,full_file)
	if val:
		file_content=full_file.file_to_upload.readlines()
		b=''
		for i in file_content.__iter__():
			b=b+i
		return render_to_response('index/wysiwyg_editor.html',{'a':b, 'user':request.user,'employee_who_added_file':User.objects.get(id=full_file.employee_who_added_file.employee_id_id), 'file_path':full_file.file_to_upload.path,'file_id':full_file.id})
	else:
		return redirect(index)
	pass
def view_of_create_file(request):
	return render_to_response('file/view_of_create_file.html')
@csrf_exempt
def create_file(request):
	file_content=request.POST.get('file_content')
	file_path=request.POST.get('file_path')
	path=request.POST.get('file_id')
	access=request.POST.get('access')
	u=User.objects.get(username=request.user)
	e=employee.objects.get(employee_id=u.id)
	f=file(file_path,'a')
	f.write(file_content)
	instance=my_file.objects.create(file_to_upload=f,employee_who_added_file=e, file_name=file_path, access=access)

	# return wysiwyg_editor(request,path)
	# return redirect(wysiwyg_editor(request,path))
	return render_to_response('file/create_file.html')
@csrf_exempt
def update_file(request):
	file_content=request.POST.get('file_content')
	file_path=request.POST.get('file_path')
	path=request.POST.get('file_id')
	f=file(file_path,'rw+')
	f.write(file_content)
	# return wysiwyg_editor(request,path)
	# return redirect(wysiwyg_editor(request,path))
	return render_to_response('file/update_file.html',{'file_path':file_path})
##########################################VIEW OF INDEX############################################
# @csrf_protect
def employee_already_associated_with_company_fail(request):
 	return render_to_response('index/employee_already_associated_with_company_fail.html')
 	pass
def admin_decorator_required_fail(request):
	return render_to_response('index/admin_decorator_required_fail.html')
	pass
def home_page(request):
	return render_to_response('index/home_page.html',{'user':request.user})
	pass
def view_of_sign_up(request):
	return render_to_response('index/view_of_sign_up.html')
	pass

@csrf_exempt
def sign_up(request):
	try:
		e_u=User.objects.create_user(username=request.POST.get('e_name'),password=request.POST.get('e_password'),email=request.POST.get('e_email_id'))
		# c=company.objects.get(id=3)
		e=employee.objects.create(employee_id=e_u, address=request.POST.get('e_address') ,phone_no=request.POST.get('e_phone'),fb_id=request.POST.get('e_fb_id'), twitter_id=request.POST.get('e_tw_id'))
		r=roles_emp.objects.create(roles_id=roles.objects.get(role_name='super admin'), u_id=e_u)
		e.save()
		r.save()
		user = authenticate(username=request.POST.get('e_name'), password=request.POST.get('e_password'))
		login(request, user)
		return render_to_response('company_template/view_of_create_company.html',{'r':request.user})
		pass
	except IntegrityError, e:
		error='oops this name is already taken'
		return render_to_response('index/view_of_sign_up.html',{'error':error})
	pass
def view_of_login(request):
	return render_to_response('index/view_of_login.html',{'r':request.user})
@login_required
@employee_already_associated_with_company
def index(request):
	a=User.objects.get(username=request.user)
	e=employee.objects.get(employee_id=a.id)
	f=my_file.objects.filter(employee_who_added_file=e)
	return render_to_response('index/index.html',{'files':f},context_instance=RequestContext(request))
@csrf_exempt
def mylogin(request):
	user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
	a='unsuccessful'
	if user is not None:
		if user.is_active:
			login(request, user)
			a=User.objects.get(username=request.POST.get('username'))
			e=employee.objects.get(employee_id=a.id)
			f=my_file.objects.filter(employee_who_added_file=e)
			return redirect(index)
			return render_to_response('index/index.html',{'files':f})
		else:
			return render_to_response('index/home_page.html')
	else:
		return render_to_response('index/home_page.html',{'a':a})
def view_of_logout(request):
	return render_to_response('index/view_of_logout.html')
def mylogout(request):
	logout(request)
	return render_to_response('index/home_page.html')
# @admin_decorator_required
@csrf_exempt
def test(request):
	json_data = json.dumps({"HTTPRESPONSE":1})
	return HttpResponse(json_data, mimetype="application/json")
	# return render_to_response
@csrf_exempt
def save_newt(request):
	s=request.POST.get('f_name')
	f=os.mkdir(s)
	user=User.objects.get(username=request.user)
	emp=employee.objects.get(employee_id=user)		
	instance=my_file(file_to_upload=f,employee_who_added_file= emp, file_name=s)
	instance.save()
	return render_to_response('index/save_newt.html')
def fail(request):
	return render_to_response('index/fail.html',context_instance=RequestContext(request))
################################view of search#######################################
import subprocess
def my_search_process(c_id,query,e_id):
	try:
		a=os.path.join("/home/sawan/Desktop/instashare/media/company_%d" %c_id,"user_%d" %e_id)
		if not subprocess.check_call(["grep","-R","-l", query,a]):
			search=subprocess.check_output(["grep","-R", "-l", query,a]).split("/home/sawan/Desktop/instashare/")
			return search
	except CalledProcessError:
		return None
	pass
def search_result(request):
	e_id=employee.objects.get(employee_id=User.objects.get(username=request.user))
	query=request.GET.get("query")
	s=request.GET.get("search_option")
	result=where_to_Search(request)
	# result=search_process(e_id.company_id_id,query)
	return render_to_response('index/search_result.html',{'a':result, 's':s},context_instance=RequestContext(request))
	pass
def where_to_Search(request):
	e=employee.objects.get(employee_id=User.objects.get(username=request.user))
	query=request.GET.get("query")
	s=request.GET.get("search_option")
	result=9
	if s=='My':
		result=my_search_process(e.company_id_id,query,e.id)
	elif s=='Private':
		result=private_search_process(e.company_id_id,query,e.id)
		pass
	elif s=='Company':
		result=company_search_process(e.company_id_id,query,e.id)
	else:
		result=public_search_process(query)
	return result
	pass
def private_search_process(c_id,query,e_id):
	try:
		a=os.path.join("/home/sawan/Desktop/instashare/media/company_%d" %c_id,"user_%d" %e_id,"PRIVATE")
		if not subprocess.check_call(["grep","-R","-l", query,a]):
			search=subprocess.check_output(["grep","-R", "-l", query,a]).split("/home/sawan/Desktop/instashare/")
			return search
	except CalledProcessError:
		return None
def company_search_process(c_id,query,e_id):
	try:
		a=os.path.join("/home/sawan/Desktop/instashare/media/company_%d" %c_id,"user_%d" %e_id,"COMPANY")
		if not subprocess.check_call(["grep","-R","-l", query,a]):
			search=subprocess.check_output(["grep","-R", "-l", query,a]).split("/home/sawan/Desktop/instashare/")
			return search
	except CalledProcessError:
		return None
def public_search_process(query):
	try:
		os.chdir('/home/sawan/Desktop/instashare/')
		if not subprocess.check_call(('find','-name','PUBLIC','-exec','grep','-R','-Hn',query,'{}',';')):
			search=subprocess.check_output(['find', '-name', 'PUBLIC', '-exec', 'grep', '-R','-l', '-Hn', query, '{}', ';']).split("./")
			return search
	except CalledProcessError:
		return None
	pass