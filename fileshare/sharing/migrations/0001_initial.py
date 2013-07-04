# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'company'
        db.create_table(u'sharing_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone_no', self.gf('django.db.models.fields.CharField')(max_length=14)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('fb_id', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('twitter_id', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'sharing', ['company'])

        # Adding model 'employee'
        db.create_table(u'sharing_employee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sharing.company'])),
            ('employee_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('project_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('project_desc', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone_no', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('fb_id', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('twitter_id', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'sharing', ['employee'])

        # Adding model 'roles'
        db.create_table(u'sharing_roles', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('role_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'sharing', ['roles'])

        # Adding model 'roles_emp'
        db.create_table(u'sharing_roles_emp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('roles_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sharing.roles'])),
            ('u_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'sharing', ['roles_emp'])

        # Adding model 'my_file'
        db.create_table(u'sharing_my_file', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employee_who_added_file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sharing.employee'])),
            ('file_to_upload', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'sharing', ['my_file'])


    def backwards(self, orm):
        # Deleting model 'company'
        db.delete_table(u'sharing_company')

        # Deleting model 'employee'
        db.delete_table(u'sharing_employee')

        # Deleting model 'roles'
        db.delete_table(u'sharing_roles')

        # Deleting model 'roles_emp'
        db.delete_table(u'sharing_roles_emp')

        # Deleting model 'my_file'
        db.delete_table(u'sharing_my_file')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sharing.company': {
            'Meta': {'object_name': 'company'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'company_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'fb_id': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'twitter_id': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'sharing.employee': {
            'Meta': {'object_name': 'employee'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'company_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sharing.company']"}),
            'employee_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'fb_id': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'project_desc': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'project_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'twitter_id': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'sharing.my_file': {
            'Meta': {'object_name': 'my_file'},
            'employee_who_added_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sharing.employee']"}),
            'file_to_upload': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'sharing.roles': {
            'Meta': {'object_name': 'roles'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role_name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'sharing.roles_emp': {
            'Meta': {'object_name': 'roles_emp'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'roles_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sharing.roles']"}),
            'u_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['sharing']