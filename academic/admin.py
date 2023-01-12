from django.contrib import admin

# Register your models here.

from .models import Tests,Subjects


admin.site.register(Tests)
admin.site.register(Subjects)