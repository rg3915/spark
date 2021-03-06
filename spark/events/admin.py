from django.contrib import admin
from .models import Event, Talk, Speaker


@admin.register(Event)
class EventModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_start', 'start', 'description']


@admin.register(Talk)
class TalkModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_start', 'start', 'description']


@admin.register(Speaker)
class SpeakerModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'photo_img', 'website_link']

    def website_link(self, obj):
        return '<a href="{0}">{0}</a>'.format(obj.website)

    website_link.allow_tags = True
    website_link.short_description = 'website'

    def photo_img(self, obj):
        return '<img width="32px" src="{}" />'.format(obj.photo)

    photo_img.allow_tags = True
    photo_img.short_description = 'foto'
