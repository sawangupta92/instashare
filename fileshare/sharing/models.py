from django import forms
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
	company_id=models.ForeignKey(company, null=True)
	employee_id=models.ForeignKey(User)
	project_name=models.CharField(max_length=50)
	project_desc=models.CharField(max_length=500)
	address=models.CharField(max_length=100)
	phone_no=models.CharField(max_length=20)
	# website=models.URLField( max_length=200)
	fb_id=models.URLField(max_length=200)
	twitter_id=models.URLField(max_length=200)
	def fields_of_employee(request):
		employee_fields=employee._meta.get_all_field_names()
		return employee_fields
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
		e=employee.objects.get(id=instance.employee_who_added_file.id)
		return os.path.join(
			"company_%d" %e.company_id.id, "user_%d" % instance.employee_who_added_file.id,"%s" % instance.access, filename)
	access=models.CharField(max_length=50)
	file_to_upload=models.FileField(upload_to=get_upload_path)
	file_name=models.CharField(max_length="100")
class ExtFileField(forms.FileField):
    """
    Same as forms.FileField, but you can specify a file extension whitelist.
    
    >>> from django.core.files.uploadedfile import SimpleUploadedFile
    >>>
    >>> t = ExtFileField(ext_whitelist=(".pdf", ".txt"))
    >>>
    >>> t.clean(SimpleUploadedFile('filename.pdf', 'Some File Content'))
    >>> t.clean(SimpleUploadedFile('filename.txt', 'Some File Content'))
    >>>
    >>> t.clean(SimpleUploadedFile('filename.exe', 'Some File Content'))
    Traceback (most recent call last):
    ...
    ValidationError: [u'Not allowed filetype!']
    """
    def __init__(self, *args, **kwargs):
        ext_whitelist = kwargs.pop("ext_whitelist")
        self.ext_whitelist = [i.lower() for i in ext_whitelist]

        super(ExtFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(ExtFileField, self).clean(*args, **kwargs)
        filename = data.name
        ext = os.path.splitext(filename)[1]
        ext = ext.lower()
        if ext not in self.ext_whitelist:
            raise forms.ValidationError("Not allowed filetype!")

#-------------------------------------------------------------------------

if __name__ == "__main__":
    import doctest, datetime
    doctest.testmod()
# class upload_file(models.Model):
	# read_me = FilerFileField(null=True, blank=True)
# class file_access(models.Model):
# 	file_Id=models.ForeignKey(my_file)
# 	access=models.CharField(max_length=50)