# Create your views here.
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from sharing.models import *
from django.views.decorators.csrf import csrf_exempt
def view_of_create_company(request):
	return render_to_response('company_template/view_of_create_company.html')
@csrf_exempt
def create_company(request):
	u=User.objects.create(username=request.POST.get('name','q'),password=request.POST.get('password','q'),email=request.POST.get('email_id','q'))
	c=company.objects.create(company_id=u,address=request.POST.get('address','q') ,phone_no=request.POST.get('phone','q'), website=request.POST.get('website','q'), fb_id=request.POST.get('fb_id','q'), twitter_id=request.POST.get('twitter_id','q'))
	e=employee.objects.create(employee_id=u,address=request.POST.get('e_address','q') ,phone_no=request.POST.get('e_phone','q'),fb_id=request.POST.get('e_fb_id','q'), twitter_id=request.POST.get('e_tw_id','q'))
	r=roles_emp.objects.create(roles_id='super admin', u_id=u)
	u.save()
	c.save()
	e.save()
	r.save()
	return render_to_response('company_template/create_company.html')
def view_of_create_employee(request):
	return render_to_response('employee_template/view_of_create_employee.html')
	pass
def create_employee(request):
	u=User.objects.create(username=request.POST.get('name','q'),password=request.POST.get('password','q'),email=request.POST.get('email_id','q'))
	e=employee.objects.create(employee_id=u,address=request.POST.get('address','q') ,phone_no=request.POST.get('phone','q'),fb_id=request.POST.get('fb_id','q'), twitter_id=request.POST.get('tw_id','q'))
	r=roles_emp.objects.create(roles_id=role, u_id=u)
	u.save()
	e.save()
	r.save()
	return render_to_response('employee_template/create_company.html')
	pass