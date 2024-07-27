from django.contrib import admin

# Register your models here.
from .models import Student, Addaitems, Naturalsitems

admin.site.register(Student)
admin.site.register(Addaitems)
admin.site.register(Naturalsitems)