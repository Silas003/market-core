from django.contrib import admin
from . import models


admin.site.register(models.Category)

@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=['id','name','price','is_sold','created_at']
