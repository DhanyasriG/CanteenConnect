from django.db import models

# Create your models here.
class Student(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.EmailField(max_length=50, blank=False, unique=True)
    password=models.CharField(max_length=20,blank=False)

    class Meta:
        db_table = "student_table"