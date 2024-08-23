from django.db import models

# Create your models here.
class Restaurant(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.EmailField(max_length=50, blank=False, unique=True)
    rname=models.CharField(max_length=20,blank=False,unique=True)
    phone=models.CharField(max_length=10,blank=False,unique=True)
    password=models.CharField(max_length=15,blank=False)

    class Meta:
        db_table = "restaurant_table"
