from django.db import models
from django.contrib.auth.models import User
class company(models.Model):
	company_id=models.ForeignKey(User)
	address=models.CharField(max_length=100)
	phone_no=models.CharField(max_length=20)
	website=models.URLField( max_length=200)
	fb_id=models.URLField(max_length=200)
	twitter_id=models.URLField(max_length=200)
class employee(models.Model):
	employee_id=models.ForeignKey(User)
	project_name=models.CharField(max_length=50)
	project_desc=models.CharField(max_length=500)
	address=models.CharField(max_length=100)
	phone_no=models.CharField(max_length=20)
	website=models.URLField( max_length=200)
	fb_id=models.URLField(max_length=200)
	twitter_id=models.URLField(max_length=200)