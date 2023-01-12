from django.contrib import admin

# Register your models here.

from .models import Tests,Subjects,Topics


admin.site.register(Tests)
admin.site.register(Subjects)
admin.site.register(Topics)