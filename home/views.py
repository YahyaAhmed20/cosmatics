from django.shortcuts import render,get_object_or_404,redirect
from .models import Slide
from .models import DiscountOffer
from services.models import SpecialService  # استيراد النموذج SpecialService
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import WhyChooseUs,Service
from accounts.views import Profile
# Create your views here.

from django.shortcuts import get_object_or_404, render
from .models import Slide, WhyChooseUs


def home(request):
    slides = Slide.objects.filter(is_active=True).order_by('id')

    # Fetch only the first active WhyChooseUs record
    why_choose_us = WhyChooseUs.objects.filter(is_active=True).first()

    service = Service.objects.filter(is_active=True)[:3]

    # الحصول على أول عرض نشط فقط
    try:
        discount_offer = DiscountOffer.objects.get(is_active=True)
    except DiscountOffer.DoesNotExist:
        discount_offer = None

    return render(request, 'home/home.html', {
        'slides': slides,
        'why_choose_us': why_choose_us,  # Pass a single object or None
        'service': service,
        'discount_offer': discount_offer
    })


@login_required
def order_summary(request, service_id):
    # جلب بيانات الخدمة باستخدام معرف الخدمة
    service = get_object_or_404(SpecialService, id=service_id)
    
    # التحقق من وجود مالك للخدمة
    doctor_name = service.owner.name if service.owner else "Not Assigned"

    # حساب السعر الإجمالي
    total_price = float(service.price)  # تحويل السعر إلى float

    # إضافة السعر الإجمالي إلى جلسة المستخدم
    request.session['total_price'] = total_price

    context = {
        'doctor_name': doctor_name,
        'service': service,
        'total_price': total_price,
    }
    return render(request, 'services/order_summary.html', context)


