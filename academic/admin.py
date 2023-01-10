from django.contrib import admin

# Register your models here.

from .models import Tests

class TestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'test_subject', 'test_title', 'month', 'test_marks', 'test_outof','submitted')
    list_filter = ('submitted', 'test_subject', 'date', 'month', 'year', 'username')
    readonly_fields = ('submitted',)
    fieldsets = (
        (None, {
            'fields': ('test_subject', 'test_title')
        }),
        ('Test Date Information', {
            'classes': ('collapse',),
            'fields': ('date', 'month', 'year')
        }),
        ('Test Marks Information', {
            'classes': ('collapse',),
            'fields': ('test_marks', 'test_outof')
        }),    
        (None, {
            'fields': ('submitted', 'username')
        }),

    )

admin.site.register(Tests, TestsAdmin)