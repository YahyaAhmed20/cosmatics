# services/admin.py

from django.contrib import admin
from .models import SpecialService,Booking

@admin.register(SpecialService)
class SpecialServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'owner')  # عرض اسم الخدمة، السعر، والمالك
    list_filter = ('owner',)  # فلترة الخدمات حسب المالك
    search_fields = ('name', 'owner__name')  # البحث باستخدام اسم الخدمة أو اسم المالك
    
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'is_paid', 'appointment_date', 'created_at')
    list_filter = ('is_paid', 'appointment_date')
    search_fields = ('user__username', 'service__name')