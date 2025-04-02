# services/admin.py

from django.contrib import admin
from .models import SpecialService

@admin.register(SpecialService)
class SpecialServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'owner')  # عرض اسم الخدمة، السعر، والمالك
    list_filter = ('owner',)  # فلترة الخدمات حسب المالك
    search_fields = ('name', 'owner__name')  # البحث باستخدام اسم الخدمة أو اسم المالك