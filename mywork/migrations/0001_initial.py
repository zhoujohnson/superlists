# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Glsx_test_case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('case_code', models.CharField(max_length=100)),
                ('case_name', models.CharField(max_length=100)),
                ('request_url', models.CharField(max_length=200)),
                ('case_desc', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Glsx_test_case_params',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('param_name', models.CharField(max_length=100)),
                ('param_value', models.CharField(max_length=100)),
                ('order', models.IntegerField()),
                ('glsx_test_case', models.ForeignKey(to='mywork.Glsx_test_case')),
            ],
        ),
        migrations.CreateModel(
            name='Glsx_test_result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('case_id', models.IntegerField(null=True, verbose_name=b'\xe7\x94\xa8\xe4\xbe\x8b\xe7\xbc\x96\xe5\x8f\xb7')),
                ('case_name', models.CharField(max_length=100, null=True, verbose_name=b'\xe7\x94\xa8\xe4\xbe\x8b\xe5\x90\x8d\xe7\xa7\xb0')),
                ('request_url', models.TextField(null=True, verbose_name=b'\xe8\xaf\xb7\xe6\xb1\x82\xe7\x9a\x84URL')),
                ('response_content', models.TextField(null=True, verbose_name=b'\xe5\x93\x8d\xe5\xba\x94\xe5\x86\x85\xe5\xae\xb9')),
                ('request_time', models.CharField(max_length=100, null=True, verbose_name=b'\xe8\xaf\xb7\xe6\xb1\x82\xe6\x97\xb6\xe9\x97\xb4')),
                ('response_time', models.CharField(max_length=100, null=True, verbose_name=b'\xe5\x93\x8d\xe5\xba\x94\xe6\x97\xb6\xe9\x97\xb4')),
                ('cost', models.CharField(max_length=100, null=True, verbose_name=b'\xe8\x80\x97\xe6\x97\xb6(ms)')),
                ('response_code', models.CharField(max_length=100, null=True, verbose_name=b'\xe5\x93\x8d\xe5\xba\x94\xe7\xa0\x81')),
                ('expectValue', models.TextField(null=True, verbose_name=b'\xe9\xa2\x84\xe6\x9c\x9f\xe7\xbb\x93\xe6\x9e\x9c')),
                ('execute_condition', models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x83\x85\xe5\x86\xb5')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
