from django.contrib import admin
# from path.to.your.module import ExportCsvMixin

from apps.models import User

# Define or import ExportCsvMixin
# class ExportCsvMixin:
#     def export_as_csv(self, request, queryset):
#         import csv
#         from django.http import HttpResponse
#
#         meta = self.model._meta
#         field_names = [field.name for field in meta.fields]
#
#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
#         writer = csv.writer(response)
#
#         writer.writerow(field_names)
#         for obj in queryset:
#             writer.writerow([getattr(obj, field) for field in field_names])
#
#         return response
#
#     export_as_csv.short_description = "Export Selected as CSV"

#@admin.register(User)
#class UserAdmin(admin.ModelAdmin):
   # list_per_page = 1  - ас попросили увеличить количество героев, которых можно увидеть на одной странице, до 250.
    #(По умолчанию 100). Вы можете сделать это следующим образом:
   # list_per_page = 4


# 2
# import sys
#
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     ...
#     # sys.maxsize - Если вы хотите полностью отключить пагинацию на странице списка администратора, вы можете сделать это.
#     list_per_page = sys.maxsize
#
# 3

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['id' , 'first_name' , 'internet_display']
#     # date_hierarchy = 'added_on' - Вы можете добавить фильтрацию по дате для любого поля даты, установив date_hierarchy.:
#     # date_hierarchy = 'added_on'
#     def internet_display(self , obj):
#         data=  ",".join([internet_obj.instagram_name if internet_obj.instagram_name else "-" for internet_obj in obj.internet_profiles.all()])
#         return data
#
#     internet_display.short_description = "internet"
#
# # 4
#
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['id' , 'first_name' , 'internet_display']
#     # date_hierarchy = 'added_on' - Вы можете добавить фильтрацию по дате для любого поля даты, установив date_hierarchy.:
#     # date_hierarchy = 'added_on'
#     def internet_display(self , obj):
#         data=  ",".join([internet_obj.instagram_name if internet_obj.instagram_name else "-" for internet_obj in obj.internet_profiles.all()])
#         return data
#
#     internet_display.short_description = "internet"