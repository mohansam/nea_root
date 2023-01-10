from django.contrib import admin

# Register your models here.

from .models import Posts_Profile, Text_Post

admin.site.register(Posts_Profile)
admin.site.register(Text_Post)
