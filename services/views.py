from django.shortcuts import render,get_object_or_404
from home.models import Service
from .models import SpecialService  # استيراد النموذج SpecialService
from django.contrib.auth.decorators import login_required

# Create your views here.

# Create your views here.
def services(request):
    
    service = Service.objects.filter(is_active=True)[:20]
    

    return render(request, 'services/services.html',{'service': service})




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


# services/views.py

def payment(request):
    # جلب السعر الإجمالي من الجلسة
    total_price = request.session.get('total_price', 0)  # إذا لم يكن موجودًا، استخدم القيمة الافتراضية 0

    # التأكد من أن القيمة عدد صحيح أو عشري
    if isinstance(total_price, float):
        total_price = round(total_price, 2)  # تقريب السعر إلى رقمين عشريين

    return render(request, 'services/payment.html', {'total_price': total_price})

def payment_success(request):
    return render(request, 'services/payment_success.html')


# views.py
