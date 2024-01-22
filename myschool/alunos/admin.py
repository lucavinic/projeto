from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Aluno, Nota

admin.site.register(Aluno)
admin.site.register(Nota)