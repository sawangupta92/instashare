from django.db import models
from django.contrib.auth.models import User
from filer.fields.file import FilerFileField
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
class upload_file(models.Model):
	read_me = FilerFileField(null=True, blank=True)