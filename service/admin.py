from django.contrib import admin
from .models import Services


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'plan', 'caption_method')
    list_filter = ('type', 'plan', 'caption_method')
    search_fields = ('type',)
    list_per_page = 20


admin.site.register(Services, ServicesAdmin)
