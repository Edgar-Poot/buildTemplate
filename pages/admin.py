# Importa el módulo de administración de Django
from django.contrib import admin
from .models import Page

# PageAdmin es nuestra clase personalizada
# ModelAdmin es una clase base de Django que controla la interfaz del admin
# Herencia de clases en python
# La clase Hija hereda todo lo que tiene la clase padre
class PageAdmin(admin.ModelAdmin):
    # PageAdmin hereda todo lo que modelAdmin sabe hacer por eso puedes usar:
    list_display = ('title', 'order')

# indica que este modelo "page" debe aparecer en el panel con la clase que personaliza su apariencia.
admin.site.register(Page, PageAdmin)
