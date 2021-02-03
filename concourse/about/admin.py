from django.contrib import admin

from .models import Events

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date','slug')
    search_fields = ['title', 'text']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Events, EventAdmin)