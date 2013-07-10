from django.core.files.base import ContentFile
from django.core.files import File
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from sharing.models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from sharing.models import *
from django.template import RequestContext

############################################DECORATORS#########################################

class admin_decorator_required(object):
	def __init__(self, orig_func):
		self.orig_func = orig_func
	def __call__(self, request, *args, **kwargs):
		r_emp=roles_emp.objects.get(u_id=request.user.id)
		if roles.objects.get(id=r_emp.roles_id_id).role_name=='super admin' or roles.objects.get(id=r_emp.roles_id_id).role_name=='admin':
			return self.orig_func(request, *args, **kwargs)
		else:
			return render_to_response('index/fail.html')

####################################VIEW OF EMPLOYEE###########################################

@admin_decorator_required
def view_of_create_employee(request):#admin decorator logout
	all_objects=roles.objects.filter()
	return render_to_response('employee_template/view_of_create_employee.html',{'a':all_objects})
	pass
@admin_decorator_required
@csrf_exempt
def create_employee(request):#admin decorator logout
	u=User.objects.create_user(username=request.POST.get('name','q'),password=request.POST.get('password','q'),email=request.POST.get('email_id','q'))
	u_c=User.objects.get(username=request.POST.get('c_name','q'))
	c=company.objects.get(company_id=u_c)
	e=employee.objects.create(employee_id=u,company_id=c,address=request.POST.get('address','q') ,phone_no=request.POST.get('phone','q'),fb_id=request.POST.get('fb_id','q'), twitter_id=request.POST.get('tw_id','q'))
	r_id=roles.objects.get(role_name=request.POST.get('role','tester'))
	r=roles_emp.objects.create(roles_id=r_id,u_id=u)
	e.save()
	r.save()
	return render_to_response('employee_template/create_company.html')
	pass
@admin_decorator_required
def view_of_delete_employee(request):#logout add admin decorator
	all_objects=employee.objects.filter()
	return render_to_response('employee_template/view_of_delete_employee.html',{'a':all_objects})
@csrf_exempt
@admin_decorator_required
def delete_employee(request):#admin decorator logout
	u=User.objects.get(username=request.POST.get('employee_name','q'))
	a=employee.objects.get(employee_id=u)
	a.delete()
	return render_to_response('employee_template/delete_employee.html')
def view_of_update_employee(request):
	employee_object=employee()
	employee_fields=employee_object.fields_of_employee()
	return render_to_response('employee_template/view_of_update_employee.html',{'fields':employee_fields})	
	pass
def employee_save_update(request):
	a=employee.objects.get(employee_id=User.objects.get(username=request.user))
	setattr(a,request.GET.get('field','w'),request.GET.get('update','w'))
	a.save()
	return render_to_response('employee_template/employee_save_update.html')

###################################### VIEW OF COMPANY################################################

def view_of_create_company(request):#admin decorator logout
	return render_to_response('company_template/view_of_create_company.html')
@csrf_exempt
@admin_decorator_required
def create_company(request):#admin decorator logout
	u=User.objects.create_user(username=request.POST.get('name','q'),password=request.POST.get('password','q'),email=request.POST.get('email_id','q'))
	c=company.objects.create(company_id=u,address=request.POST.get('address','q') ,phone_no=request.POST.get('phone','q'), website=request.POST.get('website','q'), fb_id=request.POST.get('fb_id','q'), twitter_id=request.POST.get('twitter_id','q'))
	e_u=User.objects.create_user(username=request.POST.get('e_name','q'),password=request.POST.get('e_password','q'),email=request.POST.get('e_email_id','q'))
	e=employee.objects.create(employee_id=u,company_id=c,address=request.POST.get('e_address','q') ,phone_no=request.POST.get('e_phone','q'),fb_id=request.POST.get('e_fb_id','q'), twitter_id=request.POST.get('e_tw_id','q'))
	r=roles_emp.objects.create(roles_id=roles.objects.get(role_name='super admin'), u_id=u)
	u.save()
	c.save()
	e.save()
	r.save()
	return render_to_response('company_template/create_company.html')
@admin_decorator_required
def view_of_delete_company(request):#logout add admin login decorator
	all_objects=company.objects.filter()
	return render_to_response('company_template/view_of_delete_company.html',{'a':all_objects})
@csrf_exempt
@admin_decorator_required
def delete_company(request):#login also redirect to login page and logout the current user
	u=User.objects.get(username=request.POST.get('company_name','q'))
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

#########################################VIEW OF FILE##############################################

@login_required
def view_of_upload_file(request):
	return render_to_response('file/view_of_upload_file.html')
@csrf_exempt
@login_required
def upload_file(request):
	form=file_upload(request.POST, request.FILES)
	user=User.objects.get(username=request.user)
	emp=employee.objects.get(employee_id=user)
	instance=my_file(file_to_upload=request.FILES['document'],employee_who_added_file=emp)
	instance.save()
	return render_to_response('file/upload_file.html')
@login_required
def view_of_my_file(request):
	a=User.objects.get(username=request.user)
	e=employee.objects.get(employee_id=a.id)
	f=my_file.objects.filter(employee_who_added_file=e)
	return render_to_response('file/view_of_my_file.html',{'files':f},context_instance=RequestContext('u'))
	pass
def view_my_company_file(request):
	a=User.objects.get(username=request.user)
	e=employee.objects.get(employee_id=a.id)
	c=company.objects.get(id=e.company_id_id)
	emps=employee.objects.filter(company_id=c)
	for emp in emps:
		files=my_file.objects.filter(employee_who_added_file=emp)
	return render_to_response('file/view_my_company_file.html',{'files':files})
	pass
def view_of_delete_file(request):
	a=User.objects.get(username=request.user)
	e=employee.objects.get(employee_id=a.id)
	f=my_file.objects.filter(employee_who_added_file=e)
	return render_to_response('file/view_of_delete_file.html',{'files':f})
	pass
@csrf_exempt
def delete_my_file(request):
	myfile=request.POST.get('file_to_delete')
	f=my_file.objects.get(file_to_upload=myfile)
	f.delete()
	return render_to_response('file/delete_my_file.html',{'file':myfile})
	pass

##########################################VIEW OF INDEX############################################

def view_of_login(request):
	return render_to_response('index/view_of_login.html')
@login_required
def index(request):
	return render_to_response('index/index.html')
@csrf_exempt
def mylogin(request):
	user = authenticate(username=request.POST.get('username','q'), password=request.POST.get('password','q'))
	a='unsuccessful'
	if user is not None:
		if user.is_active:
			login(request, user) 
			return render_to_response('index/index.html')
		else:
			return render_to_response('index/mylogin.html',{'a':a})
	else:
		return render_to_response('index/mylogin.html',{'a':a})
def view_of_logout(request):
	return render_to_response('index/view_of_logout.html')
def mylogout(request):
	logout(request)
	return render_to_response('index/view_of_login.html')
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