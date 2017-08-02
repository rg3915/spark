from django.contrib import admin
from .models import Lecture


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'slug', 'position')
    list_filter = ('title', 'course__name',)
