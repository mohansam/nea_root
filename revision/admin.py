from django.contrib import admin

# Register your models here.

from .models import Revision

class RevisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject_resource', 'chapter_title', 'submitted')
    list_filter = ('submitted', 'subject_resource', 'chapter_no', 'username')
    readonly_fields = ('submitted',)
    fieldsets = (
        ('Subject Information', {
            'classes': ('collapse',),
            'fields': ('subject_resource', 'chapter_no', 'chapter_title')
        }),
        ('Resources URLS', {
            'classes': ('collapse',),
            'fields': ('notes', 'flashcards', 'videos')
        }),    
        (None, {
            'fields': ('submitted', 'username')
        }),

    )

admin.site.register(Revision, RevisionAdmin)