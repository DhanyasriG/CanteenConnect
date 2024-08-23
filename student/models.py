from django.db import models

# Create your models here.
class Student(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.EmailField(max_length=50, blank=False, unique=True)
    password=models.CharField(max_length=20,blank=False)

    class Meta:
        db_table = "student_table"


class Addaitems(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, unique=True)
    price = models.IntegerField(blank=False)  # No 'bank' argument
    img = models.URLField(max_length=1000, blank=False)
    stock=models.IntegerField(blank=False,default=10)
    flag = models.CharField(max_length=1, blank=False,default='F')

    class Meta:
        db_table="adda_items"






class Naturalsitems(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, unique=True)
    price = models.IntegerField(blank=False)  # No 'bank' argument
    img = models.URLField(max_length=1000, blank=False)
    flag = models.CharField(max_length=1, blank=False,default='F')
    stock = models.IntegerField(blank=False, default=10)

    class Meta:
        db_table="naturals_items"

class RaSitems(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, unique=True)
    price = models.IntegerField(blank=False)  # No 'bank' argument
    flag= models.CharField(max_length=1,blank=False)
    img = models.URLField(max_length=1000, blank=False)
    stock = models.IntegerField(blank=False, default=10)

    class Meta:
        db_table="ras_items"

class Usitems(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, unique=True)
    price = models.IntegerField(blank=False)  # No 'bank' argument
    flag= models.CharField(max_length=1,blank=False)
    img = models.URLField(max_length=1000, blank=False)
    stock = models.IntegerField(blank=False, default=10)

    class Meta:
        db_table="Us_items"