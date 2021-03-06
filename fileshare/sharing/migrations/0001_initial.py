# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'company'
        db.create_table('sharing_company', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone_no', self.gf('django.db.models.fields.CharField')(max_length=14)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('fb_id', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('twitter_id', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('sharing', ['company'])

        # Adding model 'employee'
        db.create_table('sharing_employee', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sharing.company'], null=True)),
            ('employee_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('project_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('project_desc', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone_no', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('fb_id', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('twitter_id', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('sharing', ['employee'])

        # Adding model 'roles'
        db.create_table('sharing_roles', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('role_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('sharing', ['roles'])

        # Adding model 'roles_emp'
        db.create_table('sharing_roles_emp', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('roles_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sharing.roles'])),
            ('u_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('sharing', ['roles_emp'])

        # Adding model 'tag_file'
        db.create_table('sharing_tag_file', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('sharing', ['tag_file'])

        # Adding model 'my_file'
        db.create_table('sharing_my_file', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employee_who_added_file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sharing.employee'])),
            ('access', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('file_to_upload', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('file_name', self.gf('django.db.models.fields.CharField')(max_length='100')),
        ))
        db.send_create_signal('sharing', ['my_file'])

        # Adding M2M table for field file_tag on 'my_file'
        m2m_table_name = db.shorten_name('sharing_my_file_file_tag')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('my_file', models.ForeignKey(orm['sharing.my_file'], null=False)),
            ('tag_file', models.ForeignKey(orm['sharing.tag_file'], null=False))
        ))
        db.create_unique(m2m_table_name, ['my_file_id', 'tag_file_id'])


    def backwards(self, orm):
        # Deleting model 'company'
        db.delete_table('sharing_company')

        # Deleting model 'employee'
        db.delete_table('sharing_employee')

        # Deleting model 'roles'
        db.delete_table('sharing_roles')

        # Deleting model 'roles_emp'
        db.delete_table('sharing_roles_emp')

        # Deleting model 'tag_file'
        db.delete_table('sharing_tag_file')

        # Deleting model 'my_file'
        db.delete_table('sharing_my_file')

        # Removing M2M table for field file_tag on 'my_file'
        db.delete_table(db.shorten_name('sharing_my_file_file_tag'))


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
            'file_tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sharing.tag_file']", 'symmetrical': 'False'}),
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