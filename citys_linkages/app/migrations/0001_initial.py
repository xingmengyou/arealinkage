# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-29 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BureauAreas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(blank=True, max_length=64, null=True)),
                ('parent_id', models.CharField(blank=True, max_length=64, null=True)),
                ('parent_ids', models.CharField(blank=True, max_length=2000, null=True)),
                ('name', models.CharField(max_length=100)),
                ('sort', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, max_length=1, null=True)),
                ('create_by', models.CharField(blank=True, max_length=64, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_by', models.CharField(blank=True, max_length=64, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('del_flag', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'bureau_areas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SysArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(blank=True, max_length=64, null=True)),
                ('parent_id', models.CharField(blank=True, max_length=64, null=True)),
                ('parent_ids', models.CharField(blank=True, max_length=2000, null=True)),
                ('name', models.CharField(max_length=100)),
                ('sort', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, max_length=1, null=True)),
                ('create_by', models.CharField(blank=True, max_length=64, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_by', models.CharField(blank=True, max_length=64, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('del_flag', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'sys_area',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(blank=True, max_length=64, null=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(blank=True, max_length=64, null=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(blank=True, max_length=1, null=True)),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'town',
                'managed': True,
            },
        ),
    ]