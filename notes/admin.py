from django.contrib import admin

# Register your models here.
from .models import Note, PersonalNote

admin.site.register(Note)
admin.site.register(PersonalNote)