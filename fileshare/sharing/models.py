from django.db import models, connection, transaction
from django.db import models
from django import forms
from django.contrib.auth.models import User
import os
# from filer.fields.file import FilerFileField
from django.core.files import File
class company(models.Model):
	company_id=models.ForeignKey(User)
	address=models.CharField(max_length=100)
	phone_no=models.CharField(max_length=14)
	website=models.URLField( max_length=200)
	fb_id=models.URLField(max_length=200)
	twitter_id=models.URLField(max_length=200)
	def fields_of_company(request):
		company_fields=company._meta.get_all_field_names()
		return company_fields
class employee(models.Model):
	company_id=models.ForeignKey(company)
	employee_id=models.ForeignKey(User)
	project_name=models.CharField(max_length=50)
	project_desc=models.CharField(max_length=500)
	address=models.CharField(max_length=100)
	phone_no=models.CharField(max_length=20)
	website=models.URLField( max_length=200)
	fb_id=models.URLField(max_length=200)
	twitter_id=models.URLField(max_length=200)
class roles(models.Model):
	role_name=models.CharField(max_length=20)
class roles_emp(models.Model):
	roles_id=models.ForeignKey(roles)
	u_id=models.ForeignKey(User)
class file_upload(forms.Form):
	myfile=forms.FileField()
class my_file(models.Model):
	employee_who_added_file=models.ForeignKey(employee)
	def get_upload_path(instance, filename):
		return os.path.join(
			"user_%d" % instance.employee_who_added_file.id, filename)
	file_to_upload=models.FileField(upload_to=get_upload_path)
# class upload_file(models.Model):
	# read_me = FilerFileField(null=True, blank=True)