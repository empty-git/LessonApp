from django.contrib import admin

from Themes.models import *


# Register your models here.
class ThemesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'type_lesson', 'additional_information')
    list_display_links = ( 'title',)
    search_fields = ('title',)
    list_filter = ('type_lesson',)


admin.site.register(Theme, ThemesAdmin)
