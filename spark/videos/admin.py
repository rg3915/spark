from django.contrib import admin
from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'url', 'position')
    list_filter = ('course__name',)
