from django.contrib import admin

from .models import Banner

class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'begin', 'end')
    ordering = ('id',)
    search_fields = ('name', 'url')
admin.site.register(Banner, BannerAdmin)
