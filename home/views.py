from django.shortcuts import render,get_object_or_404
from .models import Slide
from .models import DiscountOffer

from django.contrib import messages
from .models import WhyChooseUs,Service

# Create your views here.

from django.shortcuts import get_object_or_404, render
from .models import Slide, WhyChooseUs

def home(request):
    slides = Slide.objects.filter(is_active=True).order_by('id')

    try:
        why_choose_us = WhyChooseUs.objects.get(is_active=True)
    except WhyChooseUs.DoesNotExist:
        why_choose_us = None

    service = Service.objects.filter(is_active=True)[:2]

    # الحصول على أول عرض نشط فقط
    try:
        discount_offer = DiscountOffer.objects.get(is_active=True)
    except DiscountOffer.DoesNotExist:
        discount_offer = None

    return render(request, 'home/home.html', {
        'slides': slides,
        'why_choose_us': why_choose_us,
        'service': service,
        'discount_offer': discount_offer
    })


