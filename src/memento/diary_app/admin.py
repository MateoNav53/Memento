from django.contrib import admin
from . import models

# Register your models here.
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'publish_date', 'content')

admin.site.register(models.Diary, DiaryAdmin)