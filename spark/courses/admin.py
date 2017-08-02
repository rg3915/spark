from django.contrib import admin
from .models import Course, Classe, ClasseDetail


class ClasseDetailInline(admin.TabularInline):
    model = ClasseDetail
    extra = 0


@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    inlines = [ClasseDetailInline]
    list_display = ('__str__', 'slug')


admin.site.register(Course)
