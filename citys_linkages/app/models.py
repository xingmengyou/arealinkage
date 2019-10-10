# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class BureauAreas(models.Model):
    pid = models.CharField(max_length=64, blank=True, null=True,unique=True)
    parent_id = models.CharField(max_length=64, blank=True, null=True)
    parent_ids = models.CharField(max_length=2000, blank=True, null=True)
    name = models.CharField(max_length=100)
    sort = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    del_flag = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bureau_areas'


class SysArea(models.Model):
    pid = models.CharField(max_length=64, blank=True, null=True)
    parent_id = models.CharField(max_length=64, blank=True, null=True)
    parent_ids = models.CharField(max_length=2000, blank=True, null=True)
    name = models.CharField(max_length=100)
    sort = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    del_flag = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sys_area'


class Town(models.Model):
    pid = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=1, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'town'


class Test(models.Model):
    pid = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=100)


class Village(models.Model):
    pid = models.CharField(max_length=64, blank=True, null=True)
    # parent_id = models.CharField(max_length=64, blank=True, null=True)
    parent_id = models.ForeignKey(to='BureauAreas', to_field='pid', on_delete=models.CASCADE)
    parent_ids = models.CharField(max_length=2000, blank=True, null=True)
    name = models.CharField(max_length=100)
    sort = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    create_by = models.CharField(max_length=64, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=64, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    del_flag = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'village'