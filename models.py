# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Priceperhour(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    unia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.TextField(db_collation='C', blank=True, null=True)  # This field type is a guess.
    price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'priceperhour'


class Re1(models.Model):
    name = models.TextField(db_collation='C', blank=True, null=True)  # This field type is a guess.
    tbegin = models.DateTimeField(blank=True, null=True)
    tend = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 're1'


class Rezofwork(models.Model):
    uniq = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.TextField(db_collation='C', blank=True, null=True)  # This field type is a guess.
    project = models.TextField(db_collation='C', blank=True, null=True)  # This field type is a guess.
    tbegin = models.DateTimeField(blank=True, null=True)
    tend = models.DateTimeField(blank=True, null=True)
    timeofwork = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    salary = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rezofwork'


class Students(models.Model):
    id = models.IntegerField(primary_key=True)
    tbegin = models.DateTimeField(blank=True, null=True)
    tend = models.DateTimeField(blank=True, null=True)
    rez = models.DurationField(blank=True, null=True)
    sal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rez1 = models.DurationField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'


class Workerinfo(models.Model):
    uniq = models.DecimalField(unique=True, max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.TextField(db_collation='C', blank=True, null=True)  # This field type is a guess.
    price = models.SmallIntegerField(blank=True, null=True)
    workerstatus = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workerinfo'


class Workerinfo2(models.Model):
    uniq = models.DecimalField(unique=True, max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.TextField(db_collation='C', blank=True, null=True)  # This field type is a guess.
    price = models.SmallIntegerField(blank=True, null=True)
    workerstatus = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workerinfo2'


class Workerinfo3(models.Model):
    uniq = models.DecimalField(unique=True, max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.TextField(db_collation='C', blank=True, null=True)  # This field type is a guess.
    price = models.SmallIntegerField(blank=True, null=True)
    workerstatus = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workerinfo3'
