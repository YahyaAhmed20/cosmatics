# admin.py
from django.contrib import admin
from .models import Slide
from .models import WhyChooseUs, WhyChooseUsItem,DiscountOffer

# admin.py
from .models import Service
@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle')
    
    


# admin.py


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle')

@admin.register(WhyChooseUsItem)
class WhyChooseUsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'why_choose_us')
    list_filter = ('why_choose_us',)
    search_fields = ('title',)
    
    


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)


@admin.register(DiscountOffer)
class DiscountOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'discount_percentage', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)
    
