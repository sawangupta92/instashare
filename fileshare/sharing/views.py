from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from sharing.models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
def view_of_create_company(request):
	return render_to_response('company_template/view_of_create_company.html')
def create_company(request):
	u=User.objects.create(username=request.POST.get('name','q'),password=request.POST.get('password','q'),email=request.POST.get('email_id','q'))
	c=company.objects.create(company_id=u,address=request.POST.get('address','q') ,phone_no=request.POST.get('phone','q'), website=request.POST.get('website','q'), fb_id=request.POST.get('fb_id','q'), twitter_id=request.POST.get('twitter_id','q'))
	e=employee.objects.create(employee_id=u,address=request.POST.get('e_address','q') ,phone_no=request.POST.get('e_phone','q'),fb_id=request.POST.get('e_fb_id','q'), twitter_id=request.POST.get('e_tw_id','q'))
	r=roles_emp.objects.create(roles_id=roles.objects.get(role_name='super admin'), u_id=u)
	u.save()
	c.save()
	e.save()
	r.save()
	return render_to_response('company_template/create_company.html')
def view_of_create_employee(request):
	all_objects=roles.objects.filter()
	# return render_to_response('company_template/view_of_create_company.html')
	return render_to_response('employee_template/view_of_create_employee.html',{'a':all_objects})
	pass
@csrf_exempt
def create_employee(request):
	u=User.objects.create(username=request.POST.get('name','q'),password=request.POST.get('password','q'),email=request.POST.get('email_id','q'))
	e=employee.objects.create(employee_id=u,address=request.POST.get('address','q') ,phone_no=request.POST.get('phone','q'),fb_id=request.POST.get('fb_id','q'), twitter_id=request.POST.get('tw_id','q'))
	r_id=roles.objects.get(role_name=request.POST.get('role','tester'))
	r=roles_emp.objects.create(roles_id=r_id, u_id=u)
	u.save()
	e.save()
	r.save()
	return render_to_response('employee_template/create_company.html')
	pass
@login_required
def view_of_delete_company(request):
	all_objects=company.objects.filter()
	return render_to_response('company_template/view_of_delete_company.html',{'a':all_objects})
@csrf_exempt
def delete_company(request):
	u=User.objects.get(username=request.POST.get('company_name','q'))
	a=company.objects.get(company_id=u)
	a.delete()
	return render_to_response('company_template/delete_company.html')
def view_of_delete_employee(request):
	all_objects=employee.objects.filter()
	return render_to_response('employee_template/view_of_delete_employee.html',{'a':all_objects})
@csrf_exempt
def delete_employee(request):
	u=User.objects.get(username=request.POST.get('employee_name','q'))
	a=employee.objects.get(employee_id=u)
	a.delete()
	return render_to_response('employee_template/delete_employee.html')
@login_required
def view_of_update_company(request):
	company_object=company()
	company_fields=company_object.fields_of_company()
	return render_to_response('company_template/view_of_update_company.html',{'fields':company_fields})
def save_update(request):
	f=request.GET.get('field','q')
	a=User.objects.get(f=request.GET.get('update','q'))
def view_of_login(request):
	return render_to_response('index/view_of_login.html')
def index(request):
	return render_to_response('index/index.html')
@csrf_exempt
def login(request):
	user = authenticate(username=request.POST.get('username','q'), password=request.POST.get('password','q'))
	if user is not None:
		if user.is_active:
			login(request, user) 
			return render_to_response('index/login.html')
		else:
			a='unsuccessful'
			return render_to_response('index/login.html',{'a':a})
	else:
		a='unsuccessful'
		return render_to_response('index/login.html',{'a':a})
def view_of_logout(request):
	return render_to_response('index/view_of_logout.html')
def mylogout(request):
	logout(request)
	return render_to_response('index/mylogout.html')