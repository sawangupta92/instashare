# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'my_file.file_tag'
        db.add_column('sharing_my_file', 'file_tag',
                      self.gf('django.db.models.fields.CharField')(default='2', max_length=500),
                      keep_default=False)

        # Removing M2M table for field file_tag on 'my_file'
        db.delete_table(db.shorten_name('sharing_my_file_file_tag'))


    def backwards(self, orm):
        # Deleting field 'my_file.file_tag'
        db.delete_column('sharing_my_file', 'file_tag')

        # Adding M2M table for field file_tag on 'my_file'
        m2m_table_name = db.shorten_name('sharing_my_file_file_tag')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('my_file', models.ForeignKey(orm['sharing.my_file'], null=False)),
            ('tag_file', models.ForeignKey(orm['sharing.tag_file'], null=False))
        ))
        db.create_unique(m2m_table_name, ['my_file_id', 'tag_file_id'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('codename',)", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sharing.company': {
            'Meta': {'object_name': 'company'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'company_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'fb_id': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'twitter_id': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'sharing.employee': {
            'Meta': {'object_name': 'employee'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'company_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sharing.company']", 'null': 'True'}),
            'employee_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'fb_id': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'project_desc': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'project_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'twitter_id': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'sharing.my_file': {
            'Meta': {'object_name': 'my_file'},
            'access': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'employee_who_added_file': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sharing.employee']"}),
            'file_name': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'file_tag': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'file_to_upload': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'sharing.roles': {
            'Meta': {'object_name': 'roles'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role_name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'sharing.roles_emp': {
            'Meta': {'object_name': 'roles_emp'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'roles_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sharing.roles']"}),
            'u_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'sharing.tag_file': {
            'Meta': {'object_name': 'tag_file'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['sharing']