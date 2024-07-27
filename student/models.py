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
    img = models.URLField(max_length=1000, blank=True)

    class Meta:
        db_table="adda_items"


class Naturalsitems(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, unique=True)
    price = models.IntegerField(blank=False)  # No 'bank' argument
    img = models.URLField(max_length=1000, blank=True)

    class Meta:
        db_table="naturals_items"