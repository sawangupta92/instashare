# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from sharing.models import company
def view_of_create_company(request):
	return render_to_response('view_of_create_company.html')
def create_company(request):
	name=request.POST.get('name','')
	add=request.POST.get('address','')
	phone=request.POST.get('phone','')
	website=request.POST.get('website','')
	email_id=request.POST.get('email_id','')
	fb_id=request.POST.get('fb_id','')
	twitter_id=request.POST.get('twitter_id','')
	password=request.POST.get('password','')
	u=User.objects.create(username=name,password='password',email=email_id)
	u.save()
	c=company.objects.create(company_id=u,address=add ,phone_no=phone, website=website, fb_id=fb_id, twitter_id=twitter_id)
	c.save()
	return render_to_response('create_company.html')
	pass
