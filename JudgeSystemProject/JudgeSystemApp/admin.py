from django.contrib import admin

from .models import CPPQuestions, Example, JAVAQuestions, PYTHONQuestions

from .models import CQuestions

# Register your models here.

admin.site.register(CQuestions)
admin.site.register(CPPQuestions)
admin.site.register(JAVAQuestions)
admin.site.register(PYTHONQuestions)
admin.site.register(Example)