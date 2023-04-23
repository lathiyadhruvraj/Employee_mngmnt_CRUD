from django.contrib import admin
from .models import Emp

# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display = ("name", "emp_id", "working")
    list_editable = ("working",)
    search_fields = ("name",)
    list_filter = ("working",)

admin.site.register(Emp, EmpAdmin)
