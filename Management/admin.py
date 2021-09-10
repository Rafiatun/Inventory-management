from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['title','unit']



class PurchaseAdmin(admin.ModelAdmin):
    list_display=['id','product','vendor','quantity','price','total_amount','purchase_date']


class InventoryAdmin(admin.ModelAdmin):
    search_fields=['product__title','purchase_date']
    list_display=['product','purchase_quantity','sale_quantity','total_balanced_quantity','purchase_date','sale_date','purchase_product_unit']
    
class SaleAdmin(admin.ModelAdmin):
    search_fields=['product__title']
    list_display=['product','total_amount','sale_date']


admin.site.register(Vendor)
admin.site.register(Unit)
admin.site.register(Product,ProductAdmin)
admin.site.register(Purchase,PurchaseAdmin)
admin.site.register(Sale,SaleAdmin)
admin.site.register(Inventory,InventoryAdmin)
