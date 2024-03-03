from django.db import models

# Create your models here.
class WorkerInfo(models.Model):
    uniq = models.DecimalField(unique=True, max_digits=65535, decimal_places=65535, blank=True, null=True)
    name=models.TextField()
    price=models.SmallIntegerField()
    workerstatus=models.BooleanField()

    class Meta:
        managed = False
        db_table = 'workerinfo'

class Rezofwork(models.Model):
    uniq = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.TextField(db_collation='C', blank=True, null=True)  # This field type is a guess.
    project = models.TextField(db_collation='C', blank=True, null=True)  # This field type is a guess.
    tbegin = models.DateTimeField(blank=True, null=True)
    tend = models.DateTimeField(blank=True, null=True)
    timeofwork = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #salary = models.TextField(blank=True, null=True)  # This field type is a guess.
    salary = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rezofwork'
