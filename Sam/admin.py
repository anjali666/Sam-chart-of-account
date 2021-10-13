from django.contrib import admin
from .models import Category,SubCategory,ChildCategory
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ChildCategory)

# class subcategoryInline(admin.TabularInline):
#     model= subcategory
#     extra=3
# class categoryAdmin(admin.ModelAdmin):
#     list_display = ('asset_child','asset_parent')
#     list_editable =('asset_parent',)
#     fieldsets=(
#         (
#             None,{
#                 'fields':('asset_child',)
#             }
#         ),
#     )
#     inlines=(subcategoryInline,)
# admin.site.register(category,categoryAdmin)
# class productInline(admin.TabularInline):
#     model=product
#     extra=3
# class subcategoryAdmin(admin.ModelAdmin):
#     list_display=('asset_child','asset_parent')
#     list_editable =('asset_parent',)
#     fieldsets=(
#         (
#             None,{
#                 'fields':('asset_child',)
#             }
#         ),
#     )
#     inlines=(productInline,)
#     def product_count(self,obj):
#         return obj.product_set.count()
#     def get_ordering(self, request):
#         return ('asset_child','asset_parent')
# admin.site.register(subcategory,subcategoryAdmin)
# Register your models here.



