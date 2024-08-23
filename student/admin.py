from django.contrib import admin

# Register your models here.
from .models import Student, Addaitems, Naturalsitems, RaSitems, Usitems
from restaurants.models import Restaurant

admin.site.register(Student)
admin.site.register(Addaitems)
admin.site.register(Naturalsitems)
admin.site.register(RaSitems)
admin.site.register(Usitems)
admin.site.register(Restaurant)