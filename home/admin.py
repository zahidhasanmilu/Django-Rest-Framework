from django.contrib import admin
from .models import Student, Gender, Department

# Register your models here.
admin.site.register(Student)
admin.site.register(Gender)
admin.site.register(Department)
