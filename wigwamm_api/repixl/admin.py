from django.contrib import admin

# Register your models here.
from .models import RepixlImage

class RepixlImageAdmin(admin.ModelAdmin):
    list_display = ('url', 'status')

admin.site.register(RepixlImage, RepixlImageAdmin)
