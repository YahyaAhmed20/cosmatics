# services/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Booking
from django.core.mail import send_mail

@receiver(post_save, sender=Booking)
def send_appointment_email(sender, instance, created, **kwargs):
    if instance.is_paid and instance.appointment_date:
        # نبعتله الإيميل لما يتحدد ميعاد ومعاه حجز مدفوع
        send_mail(
            subject='تم تحديد موعد الخدمة',
            message=f"تم تحديد موعدك لخدمة {instance.service.name} يوم {instance.appointment_date}.",
            from_email='clinic@example.com',
            recipient_list=[instance.user.email],
            fail_silently=True
        )
