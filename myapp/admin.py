from django.contrib import admin
from .models import Service, ContactMessage


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'slug', 'order')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('order',)
    search_fields = ('title', 'summary')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'submitted_at', 'is_read')
    list_editable = ('is_read',)
    list_filter = ('is_read', 'submitted_at')
    search_fields = ('name', 'email', 'company', 'message')
    readonly_fields = ('name', 'email', 'company', 'message', 'submitted_at')
    ordering = ('-submitted_at',)