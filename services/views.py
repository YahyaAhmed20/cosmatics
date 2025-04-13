from django.shortcuts import render,get_object_or_404
from home.models import Service
from .models import SpecialService  # استيراد النموذج SpecialService
from django.contrib.auth.decorators import login_required
from .models import Booking
from django.core.mail import send_mail

# Create your views here.

# Create your views here.
def services(request):
    
    service = Service.objects.filter(is_active=True)[:20]
    

    return render(request, 'services/services.html',{'service': service})




@login_required
def order_summary(request, service_id):
    service = get_object_or_404(SpecialService, id=service_id)

    # نعمل booking جديد
    booking = Booking.objects.create(
        user=request.user,
        service=service,
        is_paid=False  # لسه مدفعش
    )

    # نحفظ ID الحجز في session علشان نستخدمه بعد الدفع
    request.session['booking_id'] = booking.id

    total_price = float(service.price)
    request.session['total_price'] = total_price

    context = {
        'doctor_name': service.owner.name if service.owner else "غير محدد",
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

@login_required
def payment_success(request):
    booking_id = request.session.get('booking_id')

    if not booking_id:
        return render(request, 'services/payment_success.html', {'error': 'لم يتم العثور على حجز'})

    booking = Booking.objects.get(id=booking_id, user=request.user)

    # نحدث حالة الحجز إنه مدفوع
    booking.is_paid = True
    booking.save()

    # (اختياري) نبعت له إيميل
    send_mail(
        subject='تم تأكيد الحجز',
        message=f"تم تأكيد حجزك لخدمة: {booking.service.name}. برجاء اختيار موعد الحضور.",
        from_email='clinic@example.com',
        recipient_list=[request.user.email],
        fail_silently=True
    )

    return render(request, 'services/payment_success.html', {'booking': booking})


# views.py


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'services/my_bookings.html', {'bookings': bookings})
