from django.contrib import admin
from . import models

admin.site.site_header = "Event Manager"
admin.site.site_title = "Event Manager"
admin.site.site_header = "Welcome to the Event Manager admin panel"

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'organizer', 'category')
    search_fields = ('title', 'organizer')
    list_filter = ('date', 'organizer')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Event, EventAdmin)


