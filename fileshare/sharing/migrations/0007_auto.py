# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field employee_id on 'file_access'
        db.delete_table(db.shorten_name(u'sharing_file_access_employee_id'))

        # Adding M2M table for field file_id on 'file_access'
        m2m_table_name = db.shorten_name(u'sharing_file_access_file_id')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('file_access', models.ForeignKey(orm[u'sharing.file_access'], null=False)),
            ('my_file', models.ForeignKey(orm[u'sharing.my_file'], null=False))
        ))
        db.create_unique(m2m_table_name, ['file_access_id', 'my_file_id'])


    def backwards(self, orm):
        # Adding M2M table for field employee_id on 'file_access'
        m2m_table_name = db.shorten_name(u'sharing_file_access_employee_id')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('file_access', models.ForeignKey(orm[u'sharing.file_access'], null=False)),
            ('employee', models.ForeignKey(orm[u'sharing.employee'], null=False))
        ))
        db.create_unique(m2m_table_name, ['file_access_id', 'employee_id'])

        # Removing M2M table for field file_id on 'file_access'
        db.delete_table(db.shorten_name(u'sharing_file_access_file_id'))


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
            'company_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sharing.company']", 'null': 'True'}),
            'employee_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'fb_id': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'project_desc': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'project_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'twitter_id': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'sharing.file_access': {
            'Meta': {'object_name': 'file_access'},
            'access': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'file_id': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['sharing.my_file']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'sharing.my_file': {
            'Meta': {'object_name': 'my_file'},
            'employee_who_added_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sharing.employee']"}),
            'file_name': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
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