from django.contrib import admin
from using_api_view.models import CategoryAV,SubCategoryAV,DeliveryAV,VendorAV

class CategoryAVAdmin(admin.ModelAdmin):
    list_display = ['id','category_name']

class SubCategoryAVAdmin(admin.ModelAdmin):
    list_display = ['id','sub_category_name']

class DeliveryAVAdmin(admin.ModelAdmin):
    list_display = ['id','delivery_address']

class VendorAVAdmin(admin.ModelAdmin):
    list_display = ['id','vendor_name']


admin.site.register(CategoryAV,CategoryAVAdmin)
admin.site.register(SubCategoryAV,SubCategoryAVAdmin)
admin.site.register(DeliveryAV,DeliveryAVAdmin)
admin.site.register(VendorAV,VendorAVAdmin)
