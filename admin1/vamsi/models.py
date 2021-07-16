from django.db import models

# Create your models here.
class student(models.Model):
    stuid=models.IntegerField(primary_key=True)
    stuname=models.CharField(max_length=200)
    stumobileno=models.IntegerField()
    stuaddress=models.TextField()
class employee(models.Model):
    empid = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=200)
    empmobileno = models.IntegerField()
    empaddress = models.TextField()
class HR(models.Model):
    HRid = models.IntegerField(primary_key=True)
    HRname = models.CharField(max_length=200)
    HRmobileno = models.IntegerField()
    HRaddress = models.TextField()