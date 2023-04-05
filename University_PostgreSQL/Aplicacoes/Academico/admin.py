from django.contrib import admin
from .models import Curso

# Register your models here.
# admin.site.register(Curso)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cor', 'creditos')
    # list_editable = ('dados', 'creditos')
    # ordering = ('dados',)
    # search_fields = ('dados', 'creditos')
    # list_filter = ('creditos',)

    def cursos(self, obj):
        return obj.nome.upper()
    cursos.short_description = "CURSOS"
    cursos.empty_value_display = "???"
    cursos.admin_order_field = 'nome'




"""
 fieldsets = (
        (None, {
            'fields': ('nome',)
        }),
        ('Advanced options', {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': ('creditos',),
        }),
    )
"""


#  admin.site.register(Curso, CursoAdmin)
