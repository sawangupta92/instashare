from django.core.files.base import ContentFile
from django.core.files import File
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render_to_response,redirect
from sharing.models import *
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib.auth.decorators import login_required
from sharing.models import *
from django.template import RequestContext
from django.db import IntegrityError
# django.contrib.auth.context_processors.auth
############################################DECORATORS#########################################

class employee_already_associated_with_company(object):
	def __init__(self, orig_func):
		self.orig_func = orig_func
	def __call__(self, request, *args, **kwargs):
		a=employee.objects.get(employee_id=User.objects.get(username=request.user))
		if a.company_id==None:
			return self.orig_func(request, *args, **kwargs)
		else:
			return render_to_response('index/employee_already_associated_with_company_fail.html')
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
@admin_decorator_required
@csrf_exempt
def create_employee(request):#admin decorator logout
	u=User.objects.create_user(username=request.POST.get('name'),password=request.POST.get('password'),email=request.POST.get('email_id'))
	u_c=User.objects.get(username=request.POST.get('c_name'))
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
@admin_decorator_required
def delete_company(request):#login also redirect to login page and logout the current user
	u=User.objects.get(username=request.POST.get('company_name'))
	a=company.objects.get(company_id=u)
	a.delete()
	return render_to_response('company_template/delete_company.html')
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
	# emp=employee.objects.get(employee_id=User.objects.get(username=request.user))
	# emps=company.objects.get(employee=User.objects.get(username=request.user)).employee_set.filter()
	e=employee.objects.get(employee_id=User.objects.get(username=request.user))
	emps=company.objects.get(employee=e).employee_set.filter()
	return render_to_response('company_template/company.html',{'emps':emps})
	pass

#########################################VIEW OF FILE##############################################

@login_required
def view_of_upload_file(request):#logout index delete_file view_my_file view_company_file*
	return render_to_response('file/view_of_upload_file.html')
@csrf_exempt
@login_required
def upload_file(request):#logout index delete_file view_my_file view_company_file* add_another_file 
	form=file_upload(request.POST, request.FILES)
	user=User.objects.get(username=request.user)
	emp=employee.objects.get(employee_id=user)
	instance=my_file(file_to_upload=request.FILES['document'],employee_who_added_file=emp)
	instance.save()
	return render_to_response('file/upload_file.html')
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
	files=my_file.objects.filter(employee_who_added_file__in=emps)
	return render_to_response('file/view_my_company_file.html',{'name':files})
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
	f.delete()
	return render_to_response('file/delete_my_file.html',{'file':myfile})
	pass

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
		return render_to_response('index/sign_up.html')
		pass
	except IntegrityError, e:
		error='oops this name is already taken'
		return render_to_response('index/view_of_sign_up.html',{'error':error})
	pass
def view_of_login(request):
	return render_to_response('index/view_of_login.html')
@login_required
def index(request):
	a=User.objects.get(username=request.user)
	e=employee.objects.get(employee_id=a.id)
	f=my_file.objects.filter(employee_who_added_file=e)
	return render_to_response('index/index.html',{'files':f})
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
			# index(request)
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
	return render_to_response('index/test.html',{'user':request.user})
	pass
def test1(request):
	return render_to_response('index/test1.html',{'user':request})
	pass
def fail(request):
	return render_to_response('index/fail.html',{'r':request})