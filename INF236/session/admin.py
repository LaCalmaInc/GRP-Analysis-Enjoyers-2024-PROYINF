from django.contrib import admin
from .models import ArchivoDicom
admin.site.register(ArchivoDicom)
# Register your models here.
from session.models import ArchivoDicom
admin.site.register(ArchivoDicom)