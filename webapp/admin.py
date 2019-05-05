from django.contrib import admin
from .models import Store, Purchase

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['item_name','quantity','price']
    list_editable = ['quantity','price']

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['item_name','quantity','price','total_price']

